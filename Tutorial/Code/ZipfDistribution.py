import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

zipf = np.random.zipf(a=3, size=10)
print(zipf)

# Visualization of Zipf Distribution
zipf = np.random.zipf(a=2, size=1000)

sns.distplot(zipf, hist=False)
plt.show()

