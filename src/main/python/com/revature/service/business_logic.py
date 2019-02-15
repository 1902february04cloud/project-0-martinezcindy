#!/usr/bin/env python3

from ..io.data_access import register_user, access_user_password, user_exists
# C:\Users\marti\Repositories\project-0-martinezcindy\src\main\python\com\revature\io
from getpass import getpass

current_user = ''

def register():
    user = input("Please choose a username:")
    if ..io.data_access.user_exists():
        print("Username not available. Please try again.")
        register()
    passwd = input("Please choose a password:")
    print("Thank you for banking with Cinders Bank!")
    data_access.access_user_password = passwd
    current_user = user

def login(customer):
    attempt = input("Enter your password:")
    if attempt == customers[customer]:
        current_user = customer
        x = input("Login successful. \n \n Choose an option: \
            \n *Enter 'b' to view your balance\
            \n *Enter 'w' to withdraw \
            \n *Enter 'd' to deposit\
            \n *Enter 'p' to view past transactions\
            \n *Enter 'l' to logout")
        handle_options(x)
        
def handle_options(x):
    if x == 'b':
        get_balance(current_user)
    elif x == 'w':
        pass
    elif x == 'd':
        pass
    elif x == 'p':
        pass
    elif x == 'l':
        pass
    else:
        x = input("Not a valid option. Please try again:")
        handle_options(x)
    
def try_again(a):
    if a:
        if a in customers:
            login(a)
        else:
            a = input("Login failed. Please try again")
            try_again(a)
    else:
        main()


def get_balance(user):
    return

def withdraw(user):
    return

def deposit(user):
    return

def past_transactions(user):
    return

def main():
	print('TO-DO')

if __name__ == '__main__':
	main()