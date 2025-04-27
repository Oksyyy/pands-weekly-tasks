# bank.py
# Program that reads in multiple amounts in cents, sums them up and prints out the total amount in €
# Author: Oksana Abrosimova

amount1 = int(input('Enter amount 1 (in cents): '))
amount2 = int(input('Enter amount 2 (in cents): '))
# use input() function to prompt a user to enter amounts in cents
# use int() fuction to convert the enterred amount into an integer. Input is always a string

converted_amount1 = amount1/100 
# create a new variable to format amount as required per the task description
# division by 100 converts cents into decimal point amounts which represents euro
converted_amount2 = amount2/100
# convert the second amount

final_amount = converted_amount1 + converted_amount2 
# create another variable to store the final amount
# add 2 converted amounts together for the final output

print(f'The sum of these is €{final_amount:.2f}') 
# use f-string to format the program output by passing a message & final_amount variable back to the user
# use .2f to format the output to 2 decimal places