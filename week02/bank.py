# bank.py
# Program that reads in multiple amounts in cents and then sums them up and prints out the total amount in €
# Author: Oksana Abrosimova

amount1 = int(input('Enter amount 1 (in cents): ')) ## int converts the enterred amount into an integer
amount2 = int(input('Enter amount 2 (in cents): '))

newAmount1 = amount1/100 ## division by 100 converts cents into decimal points amounts
newAmount2 = amount2/100
finalNumber = newAmount1+newAmount2 ## addition adds 2 amounts together for the final output

print(f'The sum of these is €{finalNumber}') # f-string enables formating output result by combining a message & a calculated final amount