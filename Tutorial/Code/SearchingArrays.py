import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(f"1- {np.where(arr == 5)}")
print(f"2- {np.where(arr == 4)}")
print(f"3- {np.where(arr % 2 == 0)}")
print(f"4- {np.where(arr % 2 != 0)}")
print(f"5- {np.where(arr != 5)}")
print(f"6- {np.where(arr > 5)}")


arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(f"1- {np.where(arr == 5)}")
print(f"2- {np.where(arr == 4)}")
print(f"3- {np.where(arr % 2 == 0)}")
print(f"4- {np.where(arr % 2 != 0)}")
print(f"5- {np.where(arr != 5)}")
print(f"6- {np.where(arr > 5)}")


arr = np.array([1, 2, 3, 4, 5, 5])

print(f"1- {np.searchsorted(arr, 3)}")
print(f"2- {np.searchsorted(arr, 4, side='rigth')}")
print(f"3- {np.searchsorted(arr, 5)}")
print(f"4- {np.searchsorted(arr, [1, 2, 4])}")

arr = np.array([2, 1, 3, 5])

print(f"1- {np.searchsorted(arr, 1)}")
print(f"2- {np.searchsorted(arr, 2)}")
print(f"3- {np.searchsorted(arr, [1, 2, 5])}")