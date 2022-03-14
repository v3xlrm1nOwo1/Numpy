import numpy as np

# 1. Create Ndarray: 
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

# create ndarray from tuple
arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))

# create ndarray from dis
arr = np.array({1:2, 3:4, 6:8})

print(arr)
print(type(arr))

# 2. Dimantion in Array 

# Zero dimantion array
D_0 = np.array(89)

print(D_0)
print(type(D_0))
print(D_0.ndim)

# One dimantion array 
D_1 = np.array([1, 2, 3, 4, 5])

print(D_1)
print(D_1.ndim)
print(type(D_1))

# Two dimantion array
D_2 = np.array(
	[[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]
	)
print(D_2)
print(D_2.ndim)
print(type(D_2))

# 3 dimantion array
D_3 = np.array(
	[
	[[11, 22, 33], [44, 55, 66]],
	[[77, 88, 99], [10, 20, 30]],
	[[12, 13, 14], [15, 16, 17]]
	]
	)
print(D_3)
print(D_3.ndim)
print(type(D_3))


# 3. Create Dimation 
arr = np.array([1, 2, 3, 4, 5], ndmin=32)
print(arr)
print(arr.ndim)
print(type(arr))
