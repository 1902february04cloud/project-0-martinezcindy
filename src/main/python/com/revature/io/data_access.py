#!/usr/bin/env python3

import os, sys
from pathlib import Path

def register_user(username, password):
	user_data = open(username + ".txt", "w")
	user_data.write("pass:"+ password)
	user_data.close()

def access_user_password(username):
	user_data = open(username)
	return user_data.read()

def user_exists(username):
	u = Path("/"+username+".txt")
	return u.is_file()

# def main():
# 	print('TO-DO')

# if __name__ == '__main__':
# 	main()