import numpy as np


# version numpy
print(np.__version__)


# Creat Object array in numpy (ndarray)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(f"Type Object Array in Numpy: {type(arr)}")


# 0-D Array
arr = np.array(30)

print(f"array: {arr}")
print(f"Dimanstion Array: {arr.ndim}")


# 1-D Array
arr = np.array([1, 2, 3, 4, 5])

print(f"Array: {arr}")
print(f"Dimanstion Array: {arr.ndim}")


# 2-D Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(f"Array: {arr}")
print(f"Dimanstion Array: {arr.ndim}")


# 3-D Array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(f"Array: {arr}")
print(f"Dimanstion Array: {arr.ndim}")


# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4, 5], ndmin=10)

print(f"Array: {arr}")
print(f"Dimanstion Array: {arr.ndim}")
