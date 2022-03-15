import numpy as np



arr = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5])

print(np.array_split(arr, 4))
print(np.array_split(arr, 8))
print(np.array_split(arr, 5))


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

print(np.array_split(arr, 4))
print(np.array_split(arr, 7))


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(np.array_split(arr, 5))
print(np.array_split(arr, 34))

print(np.array_split(arr, 3, axis=0))
print(np.array_split(arr, 3, axis=1))


print(np.hsplit(arr, 3))
print(np.vsplit(arr, 3))
# print(np,dsplit(arr, 3))