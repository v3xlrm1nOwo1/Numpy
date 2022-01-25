import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(arr[3:12])
print(arr[1:7])

print(arr[:12])
print(arr[4:])
print(arr[:])

print(arr[-12:-4])
print(arr[-6:-1])

print(arr[-12:10])
print(arr[-10:14])

print(arr[::3])
print(arr[::-2])


arr = np.array([[1, 2, 3, 4, 5], 
				[6, 7, 8, 9, 10], 
				[11, 12, 13, 14, 15]])

print(arr[0, 2:3])
print(arr[1, -5:-1])
print(arr[:, 1:4])
print(arr[:, 2])
print(arr[1:3, :])
print(arr[-2, 2:4])


arr = np.array([[[1, 2, 3, 4, 5], 
				 [6, 7, 8, 9, 10]], 
				[[11, 12, 13, 14, 15], 
				 [16, 17, 18, 19, 20]]])

print(arr[0, 0, 1:4])
print(arr[1, :, 4])
print(arr[:, -2, -5])
print(arr[:, :, 1:4])
print(arr[:, :, [0,4]])

