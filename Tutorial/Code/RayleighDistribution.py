import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rayleigh = np.random.rayleigh(scale=1, size=10)
print(rayleigh)

# Visualization of Rayleigh Distribution

rayleigh = np.random.rayleigh(scale=1.0, size=1000)

sns.distplot(rayleigh, hist=False, name='jj')
plt.show()
