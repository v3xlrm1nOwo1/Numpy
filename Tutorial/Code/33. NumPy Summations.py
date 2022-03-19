import numpy as np



a = np.arange(5)
b = np.arange(5, 10)
print(a, b)

# 1.
print(np.add(a, b))

# 2.
print(np.sum([a, b]))

print(np.sum([a, b], axis=1))

print(np.sum([a, b], axis=0))

# 3.
print(np.cumsum(a))
print(np.cumsum(b))

