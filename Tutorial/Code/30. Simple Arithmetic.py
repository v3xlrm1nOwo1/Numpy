import numpy as np


a = np.array([1, 3, 6, 9, -3, -6])
b = np.array([1, 2, 3, 40, -9, 5])

# 1.
print(np.add(a, b))

# 2. 
print(np.subtract(a, b))

# 3.
print(np.multiply(a, b))

# 4.
print(np.divide(a, b))

# 5.
print(np.mod(a, b))

# 6.
print(np.remainder(a, b))

# 7.
print(np.divmod(a, b))

# 8.
print(np.absolute(a))
print(np.absolute(b))

# 9.
a = np.array([1, 3, 6, 9, 3, 6])
b = np.array([1, 2, 3, 40, 9, 5])
print(np.power(b, a))

