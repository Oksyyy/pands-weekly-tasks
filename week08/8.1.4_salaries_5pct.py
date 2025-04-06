# salaries_increase.py
# Author: Oksana 
import numpy as np

min_salary = 20000
max_salary = 80000
num_of_salaries = 10

salaries = np.random.randint(min_salary, max_salary, num_of_salaries)

# Increase salaries by 5%
salaries_5pct = np.array(salaries * 1.05)

# Convert float salaries value to integers

salaries_5pct = salaries_5pct.astype(int)
print(salaries_5pct)