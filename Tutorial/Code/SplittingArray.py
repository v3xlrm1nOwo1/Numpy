import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(f'Array: \n{arr}')

print(f"1- Array: {np.array_split(arr, 5)}")
print(f"2- Array: {np.array_split(arr, 3)}")
print(f"3- Array: {np.array_split(arr, 4)}")
print(f"4- Array: {np.array_split(arr, 2)}")
print(f"5- Array: {np.array_split(arr, 6)}")


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(f"Array: \n{arr}")

print(f"6- Array: {np.array_split(arr, 6)}")
print(f"7- Array: {np.array_split(arr, 5)}")
print(f"8- Array: {np.array_split(arr, 3, axis=0)}")
print(f"1- Array: {np.array_split(arr, 3, axis=1)}")

