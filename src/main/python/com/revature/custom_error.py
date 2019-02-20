#!/usr/bin/env python3

''' 
This file contents custom errors that correspond to valuable business precautions.
Precautions included are:
	*Overdraft
	*Suspicious Deposit
	*Withdraw Limit
'''

class OverdraftError(Exception):
	"""Raised when withraw amount is larger than Balance."""
	pass

class SuspiciousDepositError(Exception):
	"""Raised when deposit amount is 10,000 or more."""
	pass

class WithdrawLimitError(Exception):
	"""Raised when withdraw amount is over user's daily withdraw limit."""
	pass
