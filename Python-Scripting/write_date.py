import datetime
with open('date_info.txt', 'a') as out_file:
    out_file.write('\n' + str(datetime.datetime.now()))

