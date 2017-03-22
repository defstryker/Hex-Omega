from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from HexOmega.settings import BASE_DIR
from .utils import get_default_password, mail_kickoff, uploaded_file_handler
from .models import Project, AdminUser, MemberUser, LeaderUser, Task
from .backends import CustomUserAuth
from .forms.login_form import LoginForm
from .forms.project_forms import CreateProjectForm
from .forms.task_forms import CreateTaskForm, LeaderUpdateTaskForm

from .Xav.user_context import url_context

import os

"""
    These views are only for testing the models, and their access
"""


def index(request):
    return render(request,
                  'users/index.html')


def login_auth_2(request):
    """
    Login page authentication using django forms.
    If easier and simpler, implement this else the
    stuff I threw together up there.
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return redirect('user_logged_in', request.user.username)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            rem = request.POST.get('rem')
            user = CustomUserAuth().authenticate(username=username, password=password)

            if user is False:
                form.errors['password'] = 'The username or password is incorrect.'
                return render(request,
                              'users/login.html',
                              {
                                  'form': form,
                                  'errors': form.errors
                              })

            if user is not None:
                print('User [{}] is logging in.'.format(user.username))
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if rem is not None:
                    request.session.set_expiry(7200)
                else:
                    request.session.get_expire_at_browser_close()
                return redirect('user_logged_in', username=username)

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def logged_in(request, username):
    if AdminUser.objects.filter(username__exact=username).count() == 1:
        return redirect('display_admin', username)
    elif LeaderUser.objects.filter(username__exact=username).count() == 1:
        return redirect('leader_home', username)
    else:
        user = MemberUser.objects.get(username__exact=username)

    return render(request,
                  'users-prev/admin_logged_in.html',
                  {'li': True,
                   'user': user})


@login_required
def jump_ship(request):
    print('jumping ship....')
    logout(request)
    return redirect('login_page')


@login_required
def delete_admin(request, username, d):
    """
        Using random, crappy, no good, templates.
        good enough for testing. Will add appropriate ones
        soon.
    """
    a = AdminUser.objects.get(username__exact=d)
    a.delete()
    print('deleted')
    return redirect('list_users', username)


@login_required
def list_users(request, username):
    return render(request, 'list.html', {'admins': AdminUser.objects.all()})


@login_required
@url_context
def get_list_of_users(request):
    """
    Display a list of admin users
    /list/
    :param request:
    :return:
    :author Caroline
    """
    admin_user_list = AdminUser.objects.order_by('pk')
    paginator = Paginator(admin_user_list, 1)  # Show 3 admin per page

    page = request.GET.get('page')
    try:
        admin_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        admin_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        admin_list = paginator.page(paginator.num_pages)
    context = {'admin_list': admin_list, 'page': page}
    return render(request, 'users/list_of_users.html', context)


# ============================================================================
# Release Me!
@login_required
def leader_home(request, username):
    user = LeaderUser.objects.get(username__exact=username)
    try:
        tasks = user.project.actionlist.task_set.all()
    # for task in Task.objects.all():
    #     print(task.title, task.action_list.project.name)
    except Exception as e:
        print('Ahhhhhh')
        tasks = None
    return render(request, 'leader_home.html', {'user': user, 'tasks': tasks})


# summer-paper-4342

# ============================================================================
# My project and tasks modules
# 2017-03-22

def get_project_path(p):
    return os.path.join(BASE_DIR,
                        os.path.join('projects', p.name + '/'))


@login_required
def create_project(request, username):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.leader = LeaderUser.objects.get(username__exact=username)
            p.save()
            path = get_project_path(p)
            os.makedirs(path, 0o755)
        return redirect('display_leader', username)
    else:
        form = CreateProjectForm()

    return render(request, 'crproj.html', {'form': form})


@login_required
def create_task(request, username):
    l = LeaderUser.objects.get(username__exact=username)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            mem_dat = form.cleaned_data.get('members')
            title = form.cleaned_data.get('title')
            est_end = form.cleaned_data.get('est_end')
            status = form.cleaned_data.get('status')
            lt = form.cleaned_data.get('to_leader')
            if lt is None:
                lt = False
            t = Task.objects.create(title=title, est_end=est_end, status=status, to_leader=lt,
                                    action_list=l.project.actionlist)
            t.save()
            for m in mem_dat:
                # print(m)
                t.members.add(m)
            t.save()
            return redirect('leader_home', username)
        else:
            print(form.errors)
    else:
        form = CreateTaskForm({'pn': l.project.name})

    return render(request, 'crtask.html', {'form': form})


@login_required
def leader_update_task(request, username, p):
    l = LeaderUser.objects.get(username__exact=username)
    if request.method == 'POST':
        form = LeaderUpdateTaskForm(request.POST, request.FILES)
        if form.is_valid():
            mem_dat = form.cleaned_data.get('members')
            title = form.cleaned_data.get('title')
            est_end = form.cleaned_data.get('est_end')
            status = form.cleaned_data.get('status')
            lt = form.cleaned_data.get('to_leader')
            if lt is None:
                lt = False
            # fix tis. Buggy now.
            t, created = Task.objects.get_or_create(title=title, est_end=est_end, status=status, to_leader=lt,
                                                    action_list=l.project.actionlist)
            t.save()
            for m in mem_dat:
                # print(m)
                t.members.add(m)
            t.save()
            file = request.FILES.get('deliverable')
            uploaded_file_handler(file, get_project_path(l.project))

            return redirect('leader_home', username)
        else:
            print(form.errors)
    else:
        form = LeaderUpdateTaskForm({'pn': l.project.name})

    return render(request, 'crtask.html', {'form': form})
    pass
