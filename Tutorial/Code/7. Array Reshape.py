import numpy as np


# Reshaping arrays:

# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.
# **Note: The product of the number of elements inside the Reshape must be equal to the number of elements of the array



arr = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5])

print(arr.reshape(4, 4, 2))
print(arr.reshape(2, 2, 2, 4))

copy_or_view = arr.reshape(4, 8)
print(copy_or_view.base)

print(arr.reshape(2, 4, -1))


arr = np.array([
 [[1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]],
 [[1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 5]]
  ])

print(arr.reshape(-1))

