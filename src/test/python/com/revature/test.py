#!/usr/bin/env python3

'''
This is your main testing script, this should call several other testing scripts on its own
'''

TESTS_EXECUTED = 0
TESTS_PASSED = 0

def main():
	print('TO-DO')
	test_string = 'testme123'
    # try:
    #     is_alpha_numeric_test(test_string)
    #     is_alpha_test(test_string) #This one raises an error
    # except AssertionError as e:
    #     print(e)
    # finally:
    #     print('{} tests passed out of {} executed.'.format(str(TESTS_PASSED), str(TESTS_EXECUTED)))

def Test(function):
    
    def test_function(test_value):
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