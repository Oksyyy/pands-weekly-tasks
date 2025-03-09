# weekday.py
# Program that outputs whether or not today is a weekday
# Author: Oksana Abrosimova



import datetime 
# import datetime module to work with dates as date objects
 
today = datetime.datetime.now()
# use datetime.datetime.now() function to assign the current date to variable today 

if today.strftime("%w") in range(1,6):
# use if function to set a condition to check what day of the week today is
# use function .strftime("%w") to get Weekday as a number 0-6, where 0 is Sunday
# use range() function to set a range from 1 to 6 (6 is not included), where 1 = Monday and 5 = Friday 
    
    print('Yes, unfortunately today is a weekday.')
    # if the current day number is foubd in the set range and satisfies the above condition, it's a weekday
else:
# if the above condition evaluation is false, then it's a weekend
    print('It is the weekend, yay!')