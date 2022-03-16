import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.uniform(low=10, high=100, size=20)
print(arr)


arr = np.random.uniform(size=1000) # DIFUALT low=0.0 and hight=1.0

sns.distplot(arr, hist=False)
plt.show()

