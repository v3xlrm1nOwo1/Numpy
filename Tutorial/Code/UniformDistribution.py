import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

uniform = np.random.uniform(low=0, high=1000, size=100)
print(uniform)


uniform= np.random.uniform(low=0, high=10000, size=1000)

sns.distplot(uniform, hist=False)
plt.show()

