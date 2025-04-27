# collatz.py
# Program that prompts a user to enter any positive integer and prints out the successive values of the following calculations:
# If the integer is even, the program divides it by 2. If it's odd, the program multiplies it by 3 and adds 1
# Author: Oksana Abrosimova

integer = int(input('Please enter a positive integer: ')) 
# prompt a user to enter a positive integer using input() function
# use int() to convert the input into an integer. Input is always a string

while integer != 1: 
# set a while loop to perform required calculations as long as the integer is not equal to 1
# when the current integer value equals 1, the while loop condition won't be met and the program stops (per task description)
    
    print(integer, end = ' ') 
    # print the current integer on the same line, separated by spaces (using end = '' function)
    
    if integer % 2 == 0:
    # use if / else statement to evaluate if the integer is an even or an odd number
    # use modulo operator % to check if the integer is an even number
    # if the remainder of the integer divided by 2 is 0, then the integer is even
        
        integer = integer // 2
        # if integer is the even number, update "integer" varible by dividing the integer by 2 (per the task instructions)
    
    else:
    # use else block to handle odd numbers
    # if integer is not an even number as checked within if statement, then it's an odd number
        
        integer = (integer * 3) + 1
        # update "integer" varible by multipliying it by 3 and adding 1 (per the task instructions)
