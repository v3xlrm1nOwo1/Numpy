import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

exponential = np.random.exponential(scale=1, size=100)
print(exponential)


# Visualization of Multinomial Distribution
exponential = np.random.exponential(scale=1, size=1000)

sns.distplot(exponential, hist=False)
plt.show()