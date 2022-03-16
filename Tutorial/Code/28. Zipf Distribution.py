import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.zipf(a=3, size=10)
print(arr)


arr = np.random.zipf(a=2, size=100)
sns.distplot(arr, hist=False)
plt.show()


