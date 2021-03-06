#!/usr/bin/env python3

'''
This is your main testing script, this should call several other testing scripts on its own
'''

import os, io
from unittest.mock import patch
import business_logic
import hashlib
# import containers

TESTS_EXECUTED = 0
TESTS_PASSED = 0
# MAIN_SCRIPT_PATH = "/python/com/revature/main.py"
# BUSINESS_LOGIC_PATH = "/python/com/revature/business_logic.py"
TEST_USER_EXISTS_PATH = 'user_data/test_user_exists.txt'
TEST_USER = "test_user_exists"

def main():
    print("====Initializing Test Environment====\n")
    test_password = "t"
    hasher = hashlib.sha224()
    hasher.update(test_password.encode('utf-8'))
    hashed_password = hasher.hexdigest()

    with open(TEST_USER_EXISTS_PATH, "w") as test_file:
        test_file.write(hashed_password+"\nBalance: 50\
            \n2019-02-20 09:36:11 Deposit of 56. New Balance: 56\
            \n2019-02-20 09:36:21 Withraw of 6. New Balance: 50")

    test_string = 'testme123'
    try:
        # register_test(test_string)
        login_logout_test(test_password)
        balance_test(TEST_USER)
        withdraw_test(test_string)
        deposit_test(test_string)
        # view_transactions_test(test_string)
        # custom_errors_test(test_string)

    except AssertionError as e:
        print(e)
    except Exception as x:
        print(x)
    finally:
        print('{} tests passed out of {} executed.'.format(str(TESTS_PASSED), str(TESTS_EXECUTED)))

def Test(function):
    
    def test_function(test_value=None):
        global TESTS_EXECUTED, TESTS_PASSED
        TESTS_EXECUTED += 1
        function(test_value)
        TESTS_PASSED += 1
    return test_function

@Test
def register_test(string):
#     assert string.isalnum(), 'Input String is not alphanumeric'
	return

@Test
def login_logout_test(passwd):
    with patch('builtins.input', side_effect="passwd"):
            business_logic.login(TEST_USER)
    
    with open(TEST_USER_EXISTS_PATH) as test_data:
        lines = test_data.readlines()
        p = lines[0]
    # print(balance)
    assert passwd in p
	

@Test
def balance_test(user):
    # with patch('sys.stdout', new=io.StringIO()) as test_stdout:
    #     business_logic.handle_options(TEST_USER, "b")
    # assert test_stdout.getvalue() == "Balance: 0\n"
    
    # with patch('builtins.input', return_vaue="l"):
    #     print("balance view attempted.")
    #     business_logic.handle_options(TEST_USER, "b")
    with open(TEST_USER_EXISTS_PATH) as test_data:
        lines = test_data.readlines()
        balance = lines[1]
    # print(balance)
        assert "Balance: 0" in lines
    
@Test
def withdraw_test(string):
    with open(TEST_USER_EXISTS_PATH) as test_data:
        lines = test_data.readlines()
        balance = lines[3]
    # print(balance)
        assert "Balance: 50" in lines

@Test
def deposit_test(string):
    with open(TEST_USER_EXISTS_PATH) as test_data:
        lines = test_data.readlines()
        balance = lines[2]
    # print(balance)
    assert "Balance: 56" in balance

@Test
def view_transactions_test(string):
	return

@Test
def custom_errors_test(string):
    # make sure file doesn't get written to for overdrafts
	return	


if __name__ == '__main__':
	main()