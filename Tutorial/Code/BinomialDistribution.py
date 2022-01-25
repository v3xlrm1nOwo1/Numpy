import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

binomial = np.random.binomial(n=1000, p=0.5, size=100)
print(binomial)

# Visualization of Poisson Distribution

binomial = np.random.binomial(n=10000, p=0.5, size=1000)

sns.distplot(binomial, kde=False)
plt.show()

