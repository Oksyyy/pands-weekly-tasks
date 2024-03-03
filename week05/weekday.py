# weekday.py
# Program that outputs whether or not today is a weekday
# Author: Oksana Abrosimova

from datetime import datetime 
# import datetime module that supports date/time functions

date = datetime.now() 
# get today's date

day_of_week = date.isoweekday()
# get the day of the week as an integer

if day_of_week < 6:
    print("Yes, unfortunately today is a weekday.")
# set a condition to evaluate if it's a weekday (days from 1 to 5)

else:
    print("It is the weekend, yay!")
# set an else statement to evaluate if it's a weekend (days 6 and 7)
