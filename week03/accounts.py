# accounts.py
# Program that reads in 10 character account number and outputs the account number showing 4 last digits
# The first 6 digits of the account number are hidden and replaced by Xs
# Author: Oksana Abrosimova

account_no = input('Please enter an 10 digit account number: ')

# last_4_digits = account_no[6:10] - Obtains the last 4 digits of an account number with the known length of 10 characters

# Obtains the last 4 digits of an acocunt number with an unknown length
last_4_digits = account_no[len(account_no)-4:len(account_no)-0]

print(f"XXXXXX{last_4_digits}")