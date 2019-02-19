#!/usr/bin/env python3
# from __future__ import print_function
# from ..io.data_access import register_user as register_user, access_user_password as access_user_password, user_exists as user_exists
# C:\Users\marti\Repositories\project-0-martinezcindy\src\main\python\com\revature\io
# from getpass import getpass
import data_access
import hashlib
from main import logger
from custom_error import WithdrawLimitError, SuspiciousDepositError, OverdraftError
# TODO Add datetime, add encrytption
# add logging to each function

WITHDRAW_LIMIT = 10,000
DEPOSIT_LIMIT = 10,000

def register():
    customer = input("Please choose a username: ")
    if data_access.user_exists(customer):
        # logger.error()TODO
        print("Username not available. Please try again.\n")
        register()
    passwd = input("Please choose a password: ") #condense lines for security / add salt TODO
    # print(passwd)
    hasher = hashlib.sha224()
    hasher.update(passwd.encode('utf-8'))
    hashed_passwd = hasher.hexdigest()
    print(hashed_passwd)
    data_access.register_user(customer, hashed_passwd)
    # current_user = x 
    print("\n\n ===Thank you for registering with Cinders Bank!===\n\nPlease login for options: \n")
    login(customer)
    # return
    # data_access.register_user(customer,passwd)

def login(customer):
    attempt = input("Enter your password: ")
    # print(attempt)
    hasher = hashlib.sha224()
    hasher.update(attempt.encode('utf-8'))
    hashed_attempt = hasher.hexdigest()
    print(hashed_attempt)
    print(data_access.access_user_password(customer))
    # if attempt == data_access.access_user_password(customer):
    if hashed_attempt==data_access.access_user_password(customer): 
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
        print(data_access.get_balance())
    elif x == 'w':
        amount = input("Enter amount to withdraw: ")
        assert amount.isdigit(), "Not a valid numeric amount."
        amount = int(amount)
        balance = int(data_access.get_balance().split()[-1])
        if amount >= WITHDRAW_LIMIT:
            raise WithdrawLimitError
        if amount > balance:
            raise OverdraftError

        data_access.withdraw(amount)     
    elif x == 'd':
        amount = input("Enter amount to deposit: ")
        assert amount.isdigit(), "Not a valid numeric amount."
        amount = int(amount)
        if amount > DEPOSIT_LIMIT:
            raise SuspiciousDepositError
        data_access.deposit(amount)
    elif x == 'p':
        print(data_access.past_transactions())
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
    

# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()