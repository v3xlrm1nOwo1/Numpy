import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Type Array: {arr.dtype}")

arr = np.array(['A', 'B', 'C'])
print(f"Array: {arr}")
print(f"Type Array: {arr.dtype}")


# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(f"Array: {arr}")
print(f"Type Array: {arr.dtype}")

arr = np.array([1, 2, 3, 4, 5], dtype=bool)
print(f"Array: {arr}")
print(f"Type Array: {arr.dtype}")


# Converting Data Type on Existing Arrays
arr = np.array([1, 2, 3, 4, 5])
arr_S = arr.astype('S')
arr_b = arr.astype(bool)
print(f"Array: {arr}")
print(f"Array String: {arr_S}")
print(f"Array Boolean: {arr_b}")
