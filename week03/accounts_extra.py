# accounts_extra.py
# Program that reads in an account number and outputs the account number with only 4 last digits visible
# Author: Oksana Abrosimova

# VIRSION_2 (Extra) - handles any length account number

account = input('Please enter an account number: ') 
# prompt the user to enter an account number using input() function

account_len = len(account) 
# use len() function to count the number of digits in the account number enterred by the user

account_len_less_last4 = len(account) - 4 
# deduct 4 digits from the account number length
# this is done so we can dynamically replace the first part of the account number with X'es (for the account number of any length) 

masked_part = account_len_less_last4 * "X"
# "X" times account_len_less_last4 allows to replace first part of the account with X'es
# multiplication of integer and string creates multiple copies of the same string character

fomatted_account = masked_part + account[account_len_less_last4 : account_len]
# combine the masked_part with the last 4 digits of the account number
# to get the last 4 digits we use slicing of the first part of the account number
# in the slicing function the first argument is the starting index 
# the second argument after semicolon is the ending index

print(fomatted_account)
# print formatted account back to the user 
