import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

poisson = np.random.poisson(lam=2, size=10)
print(poisson)

# Visualization of Poisson Distribution

poisson = np.random.poisson(lam=2, size=1000)

sns.distplot(poisson, hist=False)
plt.show()