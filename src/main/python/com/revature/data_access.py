#!/usr/bin/env python3

import os, sys
from pathlib import Path
# from business_logic import current_user 
from main import logger # add logging to each function
# CURRENT_USER = ''
USER_DATA_PATH = ""

def register_user(username, password):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH, "w") as user_data:
		user_data.write(password+"\nBalance: 0\n")
	return

def access_user_password(username):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH) as user_data:
		data = user_data.readline()
	return data

def user_exists(username):
	u = Path("/user_data/"+ username +".txt")
	print(u.is_file())
	return u.is_file()

def get_balance():
	with open(USER_DATA_PATH) as user_data:
		lines = user_data.readlines()
		balance = lines[1]
	# with open(USER_DATA_PATH,"a") as user_data_append:
	# 	user_data_append.write("get balance: \n")
	return balance

def withdraw(amount):
	# Assumes no overdraft
	with open(USER_DATA_PATH,"r") as user_data:
		lines = user_data.readlines()
	new_balance = str(int(lines[1][-1]) - amount)
	lines[1] = "Balance: "+ new_balance
	with open(USER_DATA_PATH, "w") as user_data:
		user_data.writelines(lines)
	with open(USER_DATA_PATH,"a") as user_data_append:
		user_data_append.write("Withraw of "+str(amount)+". New Balance: "+ new_balance+"\n")

def deposit(amount):
	#Assumes no deposit error
	with open(USER_DATA_PATH,"r") as user_data:
		lines = user_data.readlines()
	new_balance = str(int(lines[1][-1]) + amount)
	lines[1] = "Balance: "+ new_balance
	with open(USER_DATA_PATH, "w") as user_data:
		user_data.writelines(lines)
	with open(USER_DATA_PATH,"a") as user_data_append:
		user_data_append.write("Deposit of "+str(amount)+". New Balance: "+ new_balance+"\n")

def past_transactions():
	with open(USER_DATA_PATH, "r") as user_data:
		lines = user_data.readlines()
	return lines[2:]


# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()