import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

logistic = np.random.logistic(loc=0, scale=1, size=100)
print(logistic)

# Visualization of Logistic Distribution

logistic = np.random.logistic(loc=0, scale=1, size=1000)

sns.distplot(logistic, hist=False)
plt.show()