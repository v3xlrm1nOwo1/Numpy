import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



arr = np.random.rayleigh(scale=3, size=10)
print(arr)


arr = np.random.rayleigh(size=1000) # scale default = 0

sns.distplot(arr, hist=False)
plt.show()

