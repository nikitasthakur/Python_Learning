#!/usr/bin/env python3

# takes two args: users (list) and user (string)
def add_user(users, user):
    users.append(user)
    print("added user: {}".format(user))
    return users

    
# takes one arg: users (list)    
def print_users(users):
    for item in users:
        print(item)

        
# define a list of users       
users = ['joe','mary','bob']
print("\n\n")

# add a user, passing users (list) and user (string)
print("***** add a user")
users = add_user(users,'sara')
print("\n")

# print users, passing users (list)
print("***** print all users")
print_users(users)
print('\n\n')
input("press Enter to exit...")