import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


arr = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=6)
print(arr)


arr = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=100)

sns.distplot(arr, hist=True, kde=False)
plt.show()

