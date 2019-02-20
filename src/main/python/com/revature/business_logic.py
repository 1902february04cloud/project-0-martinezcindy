#!/usr/bin/env python3

# import getpass
import data_access
import hashlib
import logging
from custom_error import WithdrawLimitError, SuspiciousDepositError, OverdraftError
from datetime import datetime

WITHDRAW_LIMIT = 10000
DEPOSIT_LIMIT = 10000
LOGIN_ATTEMPTS = 0
logger = logging.getLogger('main')

def register():
    logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" register was called.")
    customer = input("Please choose a username: ")
    if data_access.user_exists(customer):
        print("Username not available. Please try again.\n")
        register()
    passwd = input("Please choose a password: ") #add salt TODO
    hasher = hashlib.sha224()
    hasher.update(passwd.encode('utf-8'))
    hashed_passwd = hasher.hexdigest()
    data_access.register_user(customer, hashed_passwd)
    print("\n\n ===Thank you for registering with Cinders Bank!===\n\nPlease login for options: \n")
    login(customer)

def login(customer):
    logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" login was called.")
    attempt = input("Enter your password: ")
    # print(attempt)
    hasher = hashlib.sha224()
    hasher.update(attempt.encode('utf-8'))
    hashed_attempt = hasher.hexdigest()
    if hashed_attempt==data_access.access_user_password(customer): 
        print(f'\n====== Welcome back, {customer}! ======\n')
        give_options(customer)
    else:
        global LOGIN_ATTEMPTS
        print("Login Failed. Please try again.\n ")
        if LOGIN_ATTEMPTS > 6:
            print("Too many login attempts.")
            return
        LOGIN_ATTEMPTS += 1
        login(customer)

def give_options(customer):
    x = input("Choose an option: \
            \n *Enter 'b' to view your balance\
            \n *Enter 'w' to withdraw \
            \n *Enter 'd' to deposit\
            \n *Enter 'p' to view past transactions\
            \n *Enter 'l' to logout\n")
    try:
        handle_options(customer, x)
    except SuspiciousDepositError:
        print("This is a suspicious deposit. Reported.")
    except WithdrawLimitError:
        print("This amount is over the "+ WITHDRAW_LIMIT)
    except OverdraftError:
        print("Overdraft Error. Insufficient balance.")
          
def handle_options(customer, x):
    logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" option handling was used.")
    if x == 'b':
        print(data_access.get_balance(customer))
    elif x == 'w':
        amount = input("Enter amount to withdraw: ")
        assert amount.isdigit(), "Not a valid numeric amount."
        amount = int(amount)
        balance = int(data_access.get_balance(customer).split()[-1])
        if amount >= WITHDRAW_LIMIT:
            logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Withdraw Error raised.")
            raise WithdrawLimitError
        if amount > balance:
            logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Overdraft Error raised.")
            raise OverdraftError
        data_access.withdraw(customer, amount)     
    elif x == 'd':
        amount = input("Enter amount to deposit: ")
        assert amount.isdigit(), "Not a valid numeric amount."
        amount = int(amount)
        if amount > DEPOSIT_LIMIT:
            logger.debug(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Suspicious Error raised.")
            raise SuspiciousDepositError
        data_access.deposit(customer, amount)
    elif x == 'p':
        print ("Year-Month-Day Hour-Min-Sec Action")
        for t in data_access.past_transactions(customer):
            print(t)
    elif x == 'l':
        return
    else:
        x = input("Not a valid option. Please try again: ")
        handle_options(customer, x)
    x = input("Transaction successful. Choose another option or enter 'l' to logout.\n")
    handle_options(customer, x)
    
    
