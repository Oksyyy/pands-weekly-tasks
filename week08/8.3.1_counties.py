import numpy as np
import matplotlib.pyplot as plt

# set a list of possible counties
counties = ['Dublin', 'Tipperary', 'Donelgal', 'Wexford', 'Cork', 'Kildare']

# set a list of how likely each county to be chosen. p= stands for percentage points. All percentage points should add to 100
probabilities = np.random.choice(counties, p=[0.3,0.1,0.2,0.1,0.1,0.2], size=100)

unique, counts = np.unique(probabilities, return_counts = True)
plt.pie(counts, labels = counties)
plt.legend()
plt.show()