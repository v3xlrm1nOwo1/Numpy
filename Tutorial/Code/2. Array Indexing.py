import numpy as np

# Array Indexing
# [1, 2, 3, 4, 5] <=> [1, 2, 3, 4, 5]
#  0, 1, 2, 3, 4  <=> -4, -3, -2, -1
# 1D arr[index], 2D arr[index, index], 3D arr[index, index, index]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[0])
print(arr[1])
print(arr[2])

print(arr[-1])
print(arr[-2])
print(arr[-3])

print(arr[-5] + arr[4])

arr = np.array(
   [[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]
	)

print(arr[0])
print(arr[-1])

print(arr[0, 0])
print(arr[0, 1])

print(arr[-1, -1])
print(arr[-2, -1])

print(arr[-2, 0])
print(arr[-1, 2])

arr  = np.array(
	[
	[[11, 22, 33], [44, 55, 66]],
	[[77, 88, 99], [10, 20, 30]],
	[[12, 13, 14], [15, 16, 17]]
	]
	)

print(arr[0])
print(arr[1])
print(arr[-2])

print(arr[0, 0, 0])
print(arr[1, 1, 1])

print(arr[-1, -1, -1])
print(arr[-2, -2, -2])

print(arr[0, 1, -2])
print(arr[2, 1, -1])

print(arr[-1, -2, 0])
print(arr[2, -2, 1])

