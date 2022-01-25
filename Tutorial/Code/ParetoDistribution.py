import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


pareto = np.random.pareto(a=2, size=10)
print(pareto)

# Visualization of Pareto Distribution
pareto = np.random.pareto(a=3, size=1000)

sns.distplot(pareto, hist=False)
plt.show()

