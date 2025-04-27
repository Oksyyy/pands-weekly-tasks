# es.py
# Program that reads a text file from an argument on the command line and outputs the number of "e" characters this file contains
# Author: Oksana Abrosimova

import sys
# Import sys mudule to access command-line arguments when running the program from the terminal

try: 
# use try except method to catch errors and give a useful message to a user on fixing those errors
    
    filename = sys.argv[1]
    # Set filename variable to the argument passed on command line using sys.argv function
    # Argument list starts with index 0. Program name is always the first argument 
    # File name is the second argument positioned at index 1 
    # We assume a user will pass the text file name as a second argument when calling a program

    def find_e(filename, char):
    # Create a function to count the number of occurrences of a character in a file
    # Pass the filename and character to be counted as arguments

        with open(filename, 'rt') as f:
        # open a file in read mode
        # "with" pattern ensures the file is automatically closes after reading
        
            total_count = 0
            # initiate total_count variable, which will sum the number of occurences of the character in the file 
            # start with 0 to begin counting

            for l in f:
            # loop through each line in the file - this reads the file line by line
            # the 'l in f' pattern will iterate through the entire file
                count_e = l.count(char)
                # set count_e variable that counts the number of occurences of the character (char) in each line of the file
                
                total_count = total_count + count_e
                # update total_count variable with the new count of 'char' from the current file
        
        return total_count
        # return the total count of 'char' from the entire file

    char = 'e'
    # assign a variable 'char' to 'e' to be used as part of find_e function
    
    how_many_e = find_e(filename, char)
    # call find_e() function and store the result in how_many_e
   
    print(how_many_e)
    # print the final result

# if an error was found, print a message depending on error type:
except FileNotFoundError as nf:
# for FileNotFoundError direct user to pass a valid filename 
    print(f"file {filename} not found, please enter a valid filename that exists")

except IndexError as ie:
# for ndexError direct user to pass filename as an argument
    print(f"please enter the filename as an argument")