import numpy as np



arr = np.array([1, 2, 5, 6, 3, 7])


filter_arr = [True, False, False, True, True, False]
print(arr[filter_arr])


filter_arr = []
for i in arr:
	if i % 2 == 0:
		filter_arr.append(True)
	else:
		filter_arr.append(False)

print(arr[filter_arr])



print(arr[arr % 2 == 0])
print(arr[arr % 2 != 0])
print(arr[arr >= 5])

