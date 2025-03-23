# squareroot.py
# Program that takes a positive floating-point number and outputs an approximation of its square root
# Author: Oksana Abrosimova

def sqrt(number):
# create a function to calculate the square root of a number using Newton's method
    
    guess = number 
    # initial guess of square root of a number would be the number itself
    
    next_guess = (guess + (number / guess ))/2
    # calculate next (better) guess using Newton's method fomula

    threshold = 1e-10
    # set a very small threshold that will determine when the comparison of guess and next better guess will stop

    while abs(guess**2 - number) >= threshold:
    # use while loop to repeatedly execute square root approximation 
    # continue until the difference between the square of guess and number (user input) are within the threshold 
    # use abs() to ensure the difference remain positive

        guess = next_guess
        # if while loop condition is not met, update variable guess to be equal to next_guess

        next_guess = (guess + (number / guess ))/2
        # execute next_guess calculation using updated variable guess within the Newton's frmula

    # continue finding a closer approximation of square root until the while loop condition is met
    # when it's reached a point of next_guess being within the threshold, stop while loop execution    
    
    return guess
    # return guess (square root value) to the main program 
      
number = float(input("Please enter a positive number: ")) 
# ask the user to enter a number 
# convert the user input from a string to a floating-point number for accurate calculations

num = sqrt(number) 
# call square root function

print(f"The square root of {number} is approx. {num}")
# print back a message to a user showing the number they enterred and its square root 

