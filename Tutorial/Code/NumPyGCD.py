import numpy as np

a = 20
b = 25

c = np.gcd(a, b)
print(c)

a = np.array([21, 77, 35, 28, 70])

c = np.gcd.reduce(a)
print(c)

