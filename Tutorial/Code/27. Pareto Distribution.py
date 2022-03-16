import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



arr = np.random.pareto(a=3, size=10)
print(arr)

arr = np.random.pareto(a=2, size=1000)

sns.distplot(arr, hist=True, kde=False)
plt.show()


