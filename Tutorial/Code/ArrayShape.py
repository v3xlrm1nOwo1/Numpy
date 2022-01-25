import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)

arr = np.array([[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]])
print(arr.shape)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[1, 2, 3], [4, 5, 6]]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5], ndmin=10)
print(arr.shape)

# ERROR          {    elm: 6       }   {    elm: 5         }
# arr = np.array([[1, 2, 3, 4, 5, 6], [11, 12, 13, 14, 15]])
# print(arr.shape)

