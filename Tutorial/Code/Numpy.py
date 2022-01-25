# import numpy as np
# arr = np.random.choice([3, 4, 5, 6, 7], p=[0.23, 0.0, 0.27, 0.25, 0.25], size=100)
# print(arr)

# arr = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# print(arr)

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
# sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

# plt.show()

# import numpy as np

# arr = np.random.logistic(loc=0, scale=1, size=(100))
# print(arr)
# arr2 = np.random.normal(loc=0, scale=1, size=(100))
# print(arr2)


# import numpy as np

# arr = np.random.uniform(size=(10000))
# print(max(arr))


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# arr1 = np.random.normal(loc=50, scale=5, size=(1000))
# arr2 = np.random.binomial(n=100, p=0.5, size=(1000))

# sns.distplot(arr1, hist=False, label='Normal')
# sns.distplot(arr2, hist=False, label='Binomial')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# arr = np.random.normal(size=(100))
# print(arr)

# sns.distplot(arr, hist=False)
# plt.show()

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], dtype='int8')

for i in np.nditer(a[::2], flags=['buffered'], op_dtypes=['b']):
	print(i)


for i in np.ndenumerate(a):
	print(i)