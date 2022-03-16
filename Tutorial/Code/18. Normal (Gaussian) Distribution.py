import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.normal(loc=0, scale=1, size=10)
print(arr)


arr = np.random.normal(size=1000)
sns.distplot(arr)
plt.show()