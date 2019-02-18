#!/usr/bin/env python3

# from __future__ import print_function
import business_logic
from main import logger
# add logging to each function
'''
# Controller
* "The glue between the view and the business logic."
* In this project, your view is the *console*. This package should 
contain classes which get or present data from or to the user by 
making calls to the *Service* layer.
'''
customers = {}
current_user = ''

def main():
    Welcome()
    
def Welcome():
    x = input("=== Welcome to Cinders Bank === \n \n Enter to register\n\n Or enter your username to login\n")
    if x:
        if x in customers:
            business_logic.login(x)
        else:
            a = input("Login failed. Please try again\n")
            business_logic.try_again(a)
    business_logic.register()
    current_user = x 
    print("Thank you for registering with Cinders Bank!")
    print("Please login for options: \n")
    business_logic.login(current_user)
    logout(current_user)

def logout(user):
    current_user = ''
    print("Logout successful.\n")
    print("Thank you for banking with Cinders Bank!")
    
    return



if __name__ == '__main__':
	main()