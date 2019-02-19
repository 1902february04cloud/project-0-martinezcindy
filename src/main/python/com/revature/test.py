#!/usr/bin/env python3

'''
This is your main testing script, this should call several other testing scripts on its own
'''
import os
# import ..python.com.revature.business_logic

TESTS_EXECUTED = 0
TESTS_PASSED = 0
# MAIN_SCRIPT_PATH = "/python/com/revature/main.py"
# BUSINESS_LOGIC_PATH = "/python/com/revature/business_logic.py"
import business_logic

def main():
    print("====Initializing Test Environment====\n")
    test_string = 'testme123'
    try:
        register_test(test_string)
        login_logout_test(test_string)
        balance_test(test_string)
        withdraw_test(test_string)
        deposit_test(test_string)
        view_transactions_test(test_string)
        custom_errors_test(test_string)

    except AssertionError as e:
        print(e)
    except Exception as x:
        print (x)
    finally:
        print('{} tests passed out of {} executed.'.format(str(TESTS_PASSED), str(TESTS_EXECUTED)))

def Test(function):
    
    def test_function(test_value=None):
        global TESTS_EXECUTED, TESTS_PASSED
        TESTS_EXECUTED += 1
        function(test_value)
        TESTS_PASSED += 1
    return function

@Test
def register_test(string):
#     assert string.isalnum(), 'Input String is not alphanumeric'
	return

@Test
def login_logout_test(string):
	return

@Test
def balance_test(string):
	return

@Test
def withdraw_test(string):
	return

@Test
def deposit_test(string):
	return

@Test
def view_transactions_test(string):
	return

@Test
def custom_errors_test(string):
	return	


if __name__ == '__main__':
	main()