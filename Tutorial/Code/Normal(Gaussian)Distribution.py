import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normal = np.random.normal(loc=0, scale=1, size=100)
print(normal)

normal = np.random.normal(size=1000)

sns.distplot(normal, hist=False)
plt.show()

