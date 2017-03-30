import schedule
import time
from users.utils import tasks_email_schedule, project_deadline_schedule

print('starting scheduler ...')
schedule.every().day.do(tasks_email_schedule())
schedule.every().day.do(project_deadline_schedule())

while len(schedule.jobs) > 0:
    schedule.run_pending()
    time.sleep(64800)
