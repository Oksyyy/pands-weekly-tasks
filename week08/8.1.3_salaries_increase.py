# salaries_increase.py
# Author: Oksana 
import numpy as np

min_salary = 20000
max_salary = 80000
num_of_salaries = 10

# np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_salaries)
salaries_increase = salaries + 5000
print(salaries_increase)