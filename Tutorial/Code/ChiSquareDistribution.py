import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chisquare = np.random.chisquare(df=3, size=10)
print(chisquare)

# Visualization of Chi Square Distribution
chisquare = np.random.chisquare(df=2, size=1000)

sns.distplot(chisquare, hist=False)
plt.show()

