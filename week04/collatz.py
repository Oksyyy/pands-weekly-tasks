# collatz.py
# Program that prompts a user to enter any positive integer and prints out the successive values of the following calculations:
# If the integer is even, the program divides it by 2. If it's odd, the program multiplies it by 3 and adds 1
# Author: Oksana Abrosimova


integer = int(input('Please enter a positive integer: ')) 
# prompts a user to enter a positive integer

while integer != 1: 
# using while loop to iterate integer evaluation while it's not 1
# when integer == 1, the while loop condition won't be met and the program stops
    
    print(integer, end = ' ') 
    # printing the current integer on the same line, separated by spaces (using end = '' function)
    
    if integer % 2 == 0:
    # using if function and % operator to check if integer is an even number
        
        integer = integer // 2
        # if integer is an even number, telling the program to update it by dividing by 2 as per the task instructions
    
    else:
    # if integer is not an even number as checked in line 17, then it's an odd number
        
        integer = (integer * 3) + 1
        # if integer is an odd number, telling the program to update it by multipliying it by 3 and ading 1 as per the task instructions
