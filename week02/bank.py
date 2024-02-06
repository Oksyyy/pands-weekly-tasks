# bank.py
# Program that reads in amounts and prints out the sum & currency of these amounts in a readable format
# Author: Oksana Abrosimova

amount1 = int(input('Enter amount one in cent: '))
amount2 = int(input('Enter amount two in cent: '))
print(f'€{amount1/100 + amount2/100}')