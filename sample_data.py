from users.models import *
from datetime import datetime, timedelta

from users.utils import start_schedule_thread, tasks_email_schedule
import os


def setup():
    # Create role.
    r = Role()
    r.title = 'Security Coordinator'
    r.save()

    # Create admin
    adm = AdminUser(username='G2503472', first_name='admin', last_name='man')
    adm.email = 'admin_man@example.com'
    adm.set_password('qwerty123')
    adm.save()
	
    adm1 = AdminUser(username='G1234567', first_name='test', last_name='man')
    adm1.email = 'test_man@example.com'
    adm1.set_password('qwerty123')
    adm1.save()

    adm2 = AdminUser(username='G0987654', first_name='admin', last_name='hello')
    adm2.email = 'adminman22@example.com'
    adm2.set_password('qwerty123')
    adm2.save()

    # Create leader
    l = LeaderUser(username='69497604', first_name='leader', last_name='man')
    l.email = 'leader_man@example.com'
    l.set_password('qwerty123')
    l.save()
	
	 # Create leader
    l1 = LeaderUser(username='12345678', first_name='leader', last_name='first')
    l1.email = 'firstleader@example.com'
    l1.set_password('qwerty123')
    l1.save()

    # Create project
    p = Project(name='PMT')
    p.start_date = datetime.now()
    p.end_date = datetime.now() + timedelta(days=30)
    p.leader_id = l.id
    p.save()
    p.admins.add(adm)
    p.save()
	
	
	 # Create project
    p1 = Project(name='PMT01')
    p1.start_date = datetime.now()
    p1.end_date = datetime.now() + timedelta(days=30)
    p1.leader_id = l1.id
    p1.save()
    p1.admins.add(adm)
    p1.save()

    # Create member
    m = MemberUser(username='56475644', first_name='Heracles', last_name='Alcmene')
    m.set_password('qwerty123')
    m.email = 'heracles@example.com'
    m.role_id = r.id
    m.project_id = p.id
    m.save()

    n = MemberUser(username='40475328', first_name='Perseus', last_name='Son of Danae')
    n.set_password('qwerty123')
    n.email = 'perseus@example.com'
    n.role_id = r.id
    n.project_id = p.id
    n.save()

    o = MemberUser(username='81343691', first_name='Apollo', last_name='Son of Leto')
    o.set_password('qwerty123')
    o.email = 'apollo@example.com'
    o.role_id = r.id
    o.project_id = p.id
    o.save()

    t = Task(status='Assigned', start_date=datetime.now() - timedelta(days=1),
             est_end=datetime.now() + timedelta(days=1), action_list=p.actionlist)
    t.actual_end = t.est_end
    t.title = 'Programming'
    t.save()
    t.members.add(m)
    t.members.add(n)
    t.members.add(o)
    t.to_leader = True
    t.save()

    #start_schedule_thread()
    # tasks_email_schedule()


if __name__ == '__main__':
    setup()
