import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.poisson(lam=2, size=100)
print(arr)

arr = np.random.poisson(lam=2, size=1000)

sns.distplot(arr, kde=False)
plt.show()

