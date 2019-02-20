#!/usr/bin/env python3

import os, sys
from datetime import datetime 
from pathlib import Path
# import logging
# add logging to each function TODO
# logger = logging.getLogger('main')
USER_DATA_PATH = ""

def register_user(username, password):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH, "w") as user_data:
		user_data.write(password+"\nBalance: 0\n")
	return

def user_exists(username):
	u = Path("user_data/"+ username +".txt")
	return u.is_file()

def access_user_password(username):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	if not user_exists(username):
		return
	with open(USER_DATA_PATH) as user_data:
		data = user_data.readline().replace("\n","")
	return data

def get_balance(username):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH) as user_data:
		lines = user_data.readlines()
		balance = lines[1]
	return balance

def withdraw(username, amount):
	# Assumes no overdraft
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH,"r") as user_data:
		lines = user_data.readlines()
	new_balance = str(int(lines[1].split()[-1]) - amount)
	lines[1] = "Balance: $"+ new_balance
	with open(USER_DATA_PATH, "w") as user_data:
		for l in lines:
			l = l.replace("\n", "")
			user_data.write(l+"\n")
		# user_data.writelines(lines)
	with open(USER_DATA_PATH,"a") as user_data_append:
		user_data_append.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Withraw of $"+str(amount)+". New Balance: $"+ new_balance+"\n")

def deposit(username, amount):
	#Assumes no deposit error
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH,"r") as user_data:
		lines = user_data.readlines()
	new_balance = str(int(lines[1].split()[-1]) + amount)
	lines[1] = "Balance: $"+ new_balance + "\n"
	with open(USER_DATA_PATH, "w") as user_data:
		for l in lines:
			l = l.replace("\n", "")
			user_data.write(l+"\n")
		# user_data.writelines(lines)
	with open(USER_DATA_PATH,"a") as user_data_append:
		user_data_append.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" Deposit of $"+str(amount)+". New Balance: $"+ new_balance+"\n")

def past_transactions(username):
	USER_DATA_PATH = "user_data/"+ username + ".txt"
	with open(USER_DATA_PATH, "r") as user_data:
		lines = user_data.readlines()
	return lines[2:]


# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()