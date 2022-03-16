import numpy as np



# 1. shuffle

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)
print(arr)
print(np.random.shuffle(arr))


# 2. 
arr = np.array([1, 2, 3, 4, 5])

np.random.permutation(arr)
print(arr)
print(np.random.permutation(arr))

