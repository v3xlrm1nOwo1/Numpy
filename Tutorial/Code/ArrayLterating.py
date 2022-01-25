import numpy as np


# nditer
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in np.nditer(arr):
	print(i)

print("Lterating Other Data Type:")

for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(i)


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

for i in np.nditer(arr):
	print(i)

print("Lterating Other Data Type:")

for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(i)


arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

for i in np.nditer(arr):
	print(i)

print("Lterating Other Data Type:")

for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(i)

# ndenumerate
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i, j in np.ndenumerate(arr):
	print(f"index: {i}, eleme: {j}")


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
for i, j in np.ndenumerate(arr):
	print(f"index: {i}, eleme: {j}")


arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
for i, j in np.ndenumerate(arr):
	print(f"index: {i}, eleme: {j}")

