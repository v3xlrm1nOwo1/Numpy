import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


arr = np.random.logistic(loc=1, scale=2, size=10)
print(arr)


arr = np.random.logistic(size=1000) # DEFUALT loc=0, scale=1

sns.distplot(arr, hist=False)
plt.show()

