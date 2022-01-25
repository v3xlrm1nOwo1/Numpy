import numpy as np

a = 4
b = 9

c = np.lcm(a, b)
print(c)


a = np.array([1, 2, 4, 5])

c = np.lcm.reduce(a)
print(c)

