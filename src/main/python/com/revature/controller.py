#!/usr/bin/env python3

# from __future__ import print_function
import business_logic
# import logging
# add logging to each function TODO
'''
# Controller
* "The glue between the view and the business logic."
* In this project, your view is the *console*. This package should 
contain classes which get or present data from or to the user by 
making calls to the *Service* layer.
'''

# current_user = ''

def main():
    Welcome()
    
def Welcome():
    x = input("=== Welcome to Cinders Bank === \n \n Enter to register\n\n Or enter your username to login\n")
    if x:
        business_logic.login(x)
    else:
        business_logic.register()
    logout()

def logout():
    # current_user = ''
    print("Logout successful.\n")
    print("Thank you for banking with Cinders Bank!")
    return



if __name__ == '__main__':
	main()