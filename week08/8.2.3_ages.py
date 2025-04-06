import numpy as np
import matplotlib.pyplot as plt


min_salary = 20000
max_salary = 80000
num_of_salaries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, num_of_salaries)


ages = np.random.randint(low=21, high=65, size=num_of_salaries)
y = ages * ages
plt.scatter(x=ages, y=salaries, label='Salaries')

xpoints = np.array(range(1,100))
ypoints = xpoints ** 2
plt.plot(xpoints, ypoints, color='g', label = 'Ages')
plt.xlabel('Ages')
plt.ylabel('Salaries $')
plt.legend() 
plt.title("Salaries & Ages")
# plt.show()

plt.savefig('prettier-plot.png')