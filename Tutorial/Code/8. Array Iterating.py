import numpy as np




arr = np.array([1, 2, 3, 4, 5])
for i in arr:
	print(i)


arr = np.array([
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
	])
for i in arr:
	print(i)
	for j in i:
		print(j)


arr = np.array([
	[[11, 22, 33], [44, 55, 66]],
	[[77, 88, 99], [10, 20, 30]],
	[[12, 13, 14], [15, 16, 17]]
	])

for a in arr:
	print(a)
	for b in a:
		print(b)
		for c in b:
			print(c)


arr = np.array([
 [[1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]],
 [[1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 0]]
  ])

for i in np.nditer(arr):
	print(i)


for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
	print(i)


for i in np.nditer(arr, flags=['buffered'], op_dtypes=[float]):
	print(i)

for i in np.nditer(arr[:, :, 2]):
	print(i)

for a, b in np.ndenumerate(arr):
	print(a, b)

	