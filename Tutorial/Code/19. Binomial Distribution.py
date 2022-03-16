import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.binomial(n=1000, p=0.5, size=100)
print(arr)


arr = np.random.binomial(n=10, p=0.5, size=1000)

sns.distplot(arr, hist=True, kde=False)
plt.show()

