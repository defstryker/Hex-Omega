from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm

from users.models import MemberUser, Task


class CreateTaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        ms = MemberUser.objects.filter(project__name=self.data.get('pn'))
        c = [(m.id, m.get_full_name()) for m in ms]
        self.fields['members'].choices = c

    class Meta:
        model = Task
        fields = ['title', 'status', 'est_end', 'to_leader', 'members']

        widgets = {
            # 'est_end': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'est_end': AdminDateWidget(),
            'members': forms.CheckboxSelectMultiple()
        }
        help_texts = {
            'est_end': 'Please do not change the format',
            'users': 'Hold down Control/Cmd to select more than member for the task.'
        }

    def clean(self):
        print('United Abominations')
        cleaned_data = super(ModelForm, self).clean()
        l = []
        if cleaned_data.get('members') is not None:
            for member in cleaned_data.get('members'):
                l.append(member.username)
            cleaned_data['members'] = ','.join(l)
        return cleaned_data
