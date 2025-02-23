# accounts_extra.py
# Program that reads in an account number and outputs the account number with only 4 last digits visible
# Author: Oksana Abrosimova

# VIRSION_2 (Extra) - handles any length account number

account = input('Please enter an account number: ') 

account_len = len(account) 
# counts number of digits in the account number 

account_len_less_last4 = len(account) - 4 
# counts number of digits in the account number less last 4 digits 

masked_part = account_len_less_last4 * "X"
 # "X" times account_len_less_last4 allows to replace first part of the account (with unspecified length) with X'es to align number of X'es with the number of digits

fomatted_account = masked_part + account[account_len - 4 : account_len]
# add masked_part & slice the first part of the account number leaving only last 4 digits 

print(fomatted_account)
