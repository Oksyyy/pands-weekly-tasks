# test_salaries.py
# Author: Oksana 
import numpy as np

min_salary = 20000
max_salary = 80000
num_of_salaries = 10

np.random.seed(1) # set seed for salaries to be predictable each time the program is run
salaries = np.random.randint(min_salary, max_salary, num_of_salaries)

print(salaries)
