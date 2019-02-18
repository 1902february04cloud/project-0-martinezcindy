#!/usr/bin/env python3

import os, sys
from pathlib import Path
from business_logic import current_user
USER_DATA_PATH = "user_data/"+ current_user + ".txt"
from main import logger # add logging to each function

def register_user(username, password):
	user_data = open(USER_DATA_PATH, "w")
	user_data.write(password+"\n")
	user_data.write("Balance: 0\n")
	user_data.close()

def access_user_password(username):
	user_data = open(USER_DATA_PATH)
	data = user_data.readline()
	user_data.close()
	return data

def user_exists(username):
	u = Path("/user_data/"+ username +".txt")
	return u.is_file()

def get_balance():
	with open(USER_DATA_PATH) as user_data:
		balance = user_data.readline
	with open(USER_DATA_PATH,"a") as user_data_append:
		user_data_append.write("get balance: \n")
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
	return

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
	return

def past_transactions(username):
	with open(USER_DATA_PATH, "r") as user_data:
		lines = user_data.readlines()
	return lines[2:]


# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()