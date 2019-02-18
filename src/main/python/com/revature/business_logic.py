#!/usr/bin/env python3
# from __future__ import print_function
# from ..io.data_access import register_user as register_user, access_user_password as access_user_password, user_exists as user_exists
# C:\Users\marti\Repositories\project-0-martinezcindy\src\main\python\com\revature\io
from getpass import getpass
import data_access
import hashlib
from main import logger
# TODO Add datetime, add encrytption
# add logging to each function

current_user = ''

def register():
    customer = input("Please choose a username: ")
    if data_access.user_exists(customer):
        # logger.error()TODO
        print("Username not available. Please try again.\n")
        register()
    hasher = hashlib.sha224()
    passwd = input("Please choose a password: ") #condense lines for security / add salt TODO
    hasher.update(passwd.encode('utf-8'))
    hashed_passwd = hasher.hexdigest()
    data_access.register_user(customer, hashed_passwd)
    current_user = customer

def login(customer):
    hasher = hashlib.sha224()
    attempt = getpass("Enter your password: ")
    hasher.update(attempt.encode('utf-8'))
    hashed_attempt = hasher.hexdigest()
    if hashed_attempt == data_access.access_user_password(customer): 
        current_user = customer
        print(f'====== Welcome back, {customer}! ======\n')
        x = input("Login successful. \n \n Choose an option: \
            \n *Enter 'b' to view your balance\
            \n *Enter 'w' to withdraw \
            \n *Enter 'd' to deposit\
            \n *Enter 'p' to view past transactions\
            \n *Enter 'l' to logout\n")
        handle_options(x)
    else:
            print("Login Failed. Please try again.\n ")
            login(customer)
        
def handle_options(x):
    if x == 'b':
        data_access.get_balance()
        # 
    elif x == 'w':
        amount = input("Enter amount to withdraw: ")
        data_access.withdraw(amount)
        # TODO catch format error
    elif x == 'd':
        amount = input("Enter amount to deposit: ")
        # TODO catch format error
        data_access.deposit(amount)
    elif x == 'p':
        print(data_access.past_transactions(current_user))
    elif x == 'l':
        return
    else:
        x = input("Not a valid option. Please try again: ")
        handle_options(x)
    x = input("Transaction successful. Choose another option or enter 'l' to logout.\n")
    handle_options(x)
    
def try_again(a):
    if data_access.user_exists(a):
        login(a)
    else:
        a = input("Login failed. Please try again.\n Username: ")
        try_again(a)
    

# def get_balance():
#     return data_access.get_balance()

# def withdraw():
#     return data_access.withdraw()

# def deposit():
#     return

# def past_transactions():
    # return

# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()