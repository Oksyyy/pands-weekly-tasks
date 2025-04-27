# plottask.py 
# Program that displays a histogram of a normal distribution of 1000 values and a plot of h(x)=x**3
# Author:Oksana Abrosimova

# Import requires libraries - numpy to create arrays and matplotlib for data visualisation
import numpy as np
import matplotlib.pyplot as plt

# Assign variables as per task description
mean = 5
std_dev = 2
number_of_val = 1000

# Create an array for plotting a histogram 
# Use random.normal() method to generate an array with a normal distribution
# Pass assigned variables to generate the distribution 
array = np.random.normal(loc=mean, scale=std_dev, size=number_of_val)

# Set x, y axes variables

# Use linspace() function to generate evenly spaced values for the x-axis
# linspace() takes 3 parameters: start, stop (inclusive), num (number of points to generate)
xpoints = np.linspace(1,10,100)
# y-values equal x raised to the power of 3
ypoints = xpoints ** 3

# Plot a histogram using hist() method within matplotlib library
# alpha sets transparency, color specifies the hist color, label assigns the legend label
plt.hist(array, alpha=0.6, color='blue', label='Normal Distribution')

# Plot h(x)=x^3 function
# linewidth sets the tickness of the plot line
plt.plot(xpoints, ypoints, color='y', linewidth=2.0, label= 'h(x)=x^3')

# Set axes labels. Given the task doesn't specify exact labels, we assign generic names
plt.xlabel('X values')
plt.ylabel('Y values')

# Set plot title
plt.title('Task 8 - Histogram & Plot')

# Set the legend using the labels set in hist() and plot()
plt.legend()

# Call the functoion to display the plot
plt.show()

# Commented the savefig() function that was used to save the figure as per task instructions
# plt.savefig('plottask.png')
