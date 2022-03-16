import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



arr = np.random.chisquare(df=2, size=10)
print(arr)


arr = np.random.chisquare(df=2, size=1000)

sns.distplot(arr, hist=False)
plt.show()


