import numpy as np # for creating arrays
import matplotlib.pyplot as plt # for visualizing 

# for plotting an array + range provides a sequence of values - smooth curve
# an array with just two points, i.e. np.array(1,100) will create a straight line - only two points!
xpoints = np.array(range(1,100)) 
ypoints = xpoints * xpoints # x to the power of 2

plt.plot(xpoints, ypoints)
plt.show()

