import numpy as np



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 4, 5])


print(np.where(arr == 4))
print(np.where(arr == 2))
print(np.where(arr == 5))

print(np.where(arr % 2 == 0))
print(np.where(arr % 2 != 0))
print(np.where(arr > 4))
print(np.where(arr != 4))