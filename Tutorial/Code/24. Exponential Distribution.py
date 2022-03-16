import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.exponential(scale=2, size=10)
print(arr)


arr = np.random.exponential(size=1000) # default scale=1.0

sns.distplot(arr, hist=False)
plt.show()

