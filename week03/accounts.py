# accounts.py
# Program that reads in an account number and outputs the account number with only 4 last digits visible
# Author: Oksana Abrosimova



# VIRSION_1 - handles 10 digit account number

account = input('Please enter an 10 digit account number: ') 
# using input function to prompt a user to enter a specified length account number

fomatted_account = account.replace(account[-10:-4], "XXXXXX") 
# in the above line we use two functions chained:
# account[-10:-4] is used to slice the first 6 digits using negative indexing to count from left (1st digit = -10) to right (6th digit = -4)
# account.replace() replaces sliced in the previous setp characters with 6 X'es to represent hiddent account digits

print(fomatted_account)