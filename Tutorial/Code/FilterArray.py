import numpy as np

# 1- 
arr = np.array([1, 2, 3, 4, 5])

filter = [True, False, False, True, True]
new_arr = arr[filter]
print(new_arr)

# 2- Creating the Filter Array

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filter = []

for i in arr:
	if i % 2 == 0:
		filter.append(True)
	else:
		filter.append(False)

new_arr = arr[filter]
print(new_arr)


filter = []

for i in arr:
	if i % 2 != 0:
		filter.append(True)
	else:
		filter.append(False)

new_arr = arr[filter]
print(new_arr)

# 3- Creating Filter Directly From Array
new_arr = arr[arr % 2 == 0]
print(new_arr)

new_arr = arr[arr > 5]
print(new_arr)

new_arr = arr[arr < 5]
print(new_arr)