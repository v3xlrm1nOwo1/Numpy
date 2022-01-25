import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

multinomial = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(multinomial)

# Visualization of Multinomial Distribution

sns.distplot(multinomial, hist=False)
plt.show()