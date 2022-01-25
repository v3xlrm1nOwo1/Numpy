import numpy as np

# Summations
# What is the difference between summation and addition?
# Addition is done between two arguments whereas summation happens over n elements.

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.add(a, b)
print(c)

c = np.sum(a)
print(c)

c = np.sum(b)
print(c)

c = np.sum((a, b))
print(c)

c = np.sum([a, b], axis=0)
print(c)

c = np.sum([a, b], axis=1)
print(c)


c = np.cumsum(a)
print(c)

c = np.cumsum(b)
print(c)

