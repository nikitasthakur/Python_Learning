#!/usr/bin/env python3

from crontab import CronTab

# access the system crontab
my_cron = CronTab(user='joe')

# remove my cron jobs
for job in my_cron:
    print(job)
    my_cron.remove(job)
    my_cron.write()

print("\n\ncron jobs removed...")

# my_cron.remove_all()
# my_cron.write()

