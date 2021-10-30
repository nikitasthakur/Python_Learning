#!/usr/bin/env python3

from crontab import CronTab

# access the system crontab
my_cron = CronTab(user='joe')

job = my_cron.new(command='python3 ~/139894/write_date.py')
job.minute.every(1)
my_cron.write()



# iterate through my cron jobs
for job in my_cron:
    print(job)

