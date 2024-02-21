# collatz.py
# Program that reads in any positive integer and outputs the successive values of the following calculations:
# If the current value is even, the program divides it by 2. If it's off, the program multiplies it by 3 and add 1
# The program ends if the current value = 1
# Author: Oksana Abrosimova

value = int(input("Please enter a positive integer: ")) 
# ask the user to enter any positive integer

print(value, end=" ")

while value != 1: 
# while the value enterred is not one, evaluate the value and update it's value using conditions below
    
    if (value % 2) == 0: 
    # if the value is even >>
      
       value = value // 2 # divide the value by 2 
    
    elif (value % 2) != 0: 
    # if the value is odd >>
       
       value = value * 3 + 1 # multiply the value by 3 and add 1
    
    print(value, end=" ")
    # print updated value and continue the loop

print(" ")