import numpy as np



arr = np.array([1, 4, 2, 6, 1, 9, 5])

# 1. 
print(np.diff(arr))

# 2.
print(np.diff(arr, n=2))

# 3.
print(np.diff(arr, n=3))