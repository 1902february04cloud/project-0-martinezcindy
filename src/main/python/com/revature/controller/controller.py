#!/usr/bin/env python3
from __future__ import print_function
import service.business_logic as business_logic

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
    x = input("=== Welcome to Cinders Bank === \n \n Enter to register \n \n Or enter your username to login")
    print()
    if x:
        if x in customers:
            business_logic.login(x)
        else:
            a = input("Login failed. Please try again")
            business_logic.try_again(a)
    business_logic.register()
    # input("")


def logout(user):
    current_user = ''
    return



if __name__ == '__main__':
	main()