import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.prod(a)
print(c)

c = np.prod(b)
print(c)


c = np.prod([a, b])
print(c)

c = np.prod([a, b], axis=0)
print(c)

c = np.prod([a, b], axis=1)
print(c)

c = np.cumprod(a)
print(c)

c = np.cumprod(b)
print(c)

