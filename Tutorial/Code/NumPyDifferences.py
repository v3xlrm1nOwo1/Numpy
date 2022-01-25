import numpy as np

a = np.array([4, 9, 10, 5])

c = np.diff(a)
print(c)

c = np.diff(a, n=2)
print(c)

c = np.diff(a, n=3)
print(c)

