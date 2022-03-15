import numpy as np



arr_1 = np.array([1, 2, 3])
arr_2 = np.array([6, 7, 8])

print(np.concatenate((arr_1, arr_2)))
# print(np.concatenate((arr_1, arr_2), axis=1))
print(np.concatenate((arr_1, arr_2), axis=0))


arr_1 = np.array([[1, 2, 3], [4, 9, 0]])
arr_2 = np.array([[6, 7, 8], [3, 7, 9]])

print(np.concatenate((arr_1, arr_2)))
print(np.concatenate((arr_1, arr_2), axis=1))
print(np.concatenate((arr_1, arr_2), axis=0))


print("Stack: ")
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([6, 7, 8])

print(np.stack((arr_1, arr_2)))
print(np.stack((arr_1, arr_2), axis=1))
print(np.stack((arr_1, arr_2), axis=0))


arr_1 = np.array([[1, 2, 3], [4, 9, 0]])
arr_2 = np.array([[6, 7, 8], [3, 7, 9]])

print(np.stack((arr_1, arr_2)))
print(np.stack((arr_1, arr_2), axis=1))
print(np.stack((arr_1, arr_2), axis=0))

print("H,V,D Stack:")
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([6, 7, 8])

print(np.hstack((arr_1, arr_2)))
print(np.vstack((arr_1, arr_2)))
print(np.dstack((arr_1, arr_2)))


arr_1 = np.array([[1, 2, 3], [4, 9, 0], [41, 20, 33]])
arr_2 = np.array([[6, 7, 8], [3, 7, 9], [12, 45, 89]])

print(np.hstack((arr_1, arr_2)))
print(np.vstack((arr_1, arr_2)))
print(np.dstack((arr_1, arr_2)))

