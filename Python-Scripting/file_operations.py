#!/usr/bin/env python3
import os
import datetime

def print_msg(msg):
    print("\nContents from message file:")
    for item in msg:
        print(item)

# set up the working directory, file_name, full file path
working_dir = 'PythonScripting'
file_name = 'message.txt'
my_path = os.path.join(r"C:\Users\nikita.thakur\Demos",working_dir)
my_file = os.path.join(r"C:\Users\nikita.thakur\Demos",working_dir,file_name)
my_files = os.listdir(my_path)
print("\n\n")
for filename in my_files:
    print(filename)

# open file object in readonly mode and print it using readlines()
message_file = open(my_file, 'r')
print("\n\nContents from message file: {}".format(message_file.readlines()))
input("\npress Enter to continue...\n")
message_file.close()

# open file object for appending ('w' will overwrite the existing file)
message_file = open(my_file, 'a')
message_file.write("\nFiles backed up: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
message_file.close()
message_file = open(my_file, 'r')
messages = message_file.readlines()
#print("\n\nContents from message file: {}".format(message_file.readlines()))
message_file.close()
print_msg(messages)
input("\npress Enter to exit...\n\n")