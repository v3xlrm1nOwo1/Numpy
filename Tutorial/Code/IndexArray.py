import numpy as np

# 1-D Array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Accessing the elements of 1-D Arrays using a positive index
print(arr[0])
print(arr[1])
print(arr[3])

# Accessing the elements of 1-D matrices using the negative index
print(arr[-1])
print(arr[-2])
print(arr[-3])



# 2-D Array
arr = np.array([[1, 2, 3, 4, 5], 
				[6, 7, 8, 9, 10]])

# Accessing the elements of 2-D Arrays using a positive index
print(arr[0, 0])
print(arr[1, 1])
print(arr[0, 2])
print(arr[1, 3])

# Accessing the elements of 1-D matrices using the negative index
print(arr[-1, -2])
print(arr[-2, -1])
print(arr[-1, -5])
print(arr[-2, -4])

# Accessing the elements of 1-D matrices using the negative and positive index
print(arr[0, -3])
print(arr[-2, 2])
print(arr[-1, 2])
print(arr[1, -3])


# 3-D Array
arr = np.array([
				[[1, 2, 3, 4], 
				 [5, 6, 7, 8]], 
				[[9, 10, 11, 12], 
				 [13, 14, 15, 16]]
				 ])

# Accessing the elements of 2-D Arrays using a positive index
print(arr[0, 1, 2])
print(arr[1, 0, 3])
print(arr[1, 1, 1])
print(arr[1, 1, 2])

# Accessing the elements of 1-D matrices using the negative index
print(arr[-1, -1, -2])
print(arr[-2, -2, -4])
print(arr[-2, -1, -2])
print(arr[-1, -1, -3])

# Accessing the elements of 1-D matrices using the negative and positive index
print(arr[0, 0, -1])
print(arr[-1, -2, 2])
print(arr[-1, -2, -3])
print(arr[1, 1, -1])

