import numpy as np

# NumPy Array Shape
# The shape of an array is the number of elements in each dimension.
# return tuple for count of elments for all dimantion like: (v,) OR (v, v) OR (v, v, v)

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)


arr = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
	])
print(arr.shape)


arr = np.array([
	[[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]],
	[[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
	])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5], ndmin=32)
print(arr.shape)

