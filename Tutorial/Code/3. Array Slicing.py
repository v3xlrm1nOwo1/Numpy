import numpy as np

# Array Slicing
# arr[Start:End]
# arr[Start:End:Step]
# arr[Start:] OR arr[:End] OR arr[::Step]
# Start = +, - | End = +, - | Step = +, - 


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[1:6])
print(arr[:])
print(arr[:8])
print(arr[5:])

print(arr[-9:-4])
print(arr[-6:-4])

print(arr[-8: 4])
print(arr[-5:])
print(arr[:-5])

print(arr[::3])
print(arr[::-3])
print(arr[4:-2:2])

arr = np.array(
   [[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]
	)

print(arr[1:2])
print(arr[-3:-1])
print(arr[1, 0:1])
print(arr[2, -2:-1])
print(arr[:2, 0])
print(arr[:, -3])

arr  = np.array(
	[
	[[11, 22, 33], [44, 55, 66]],
	[[77, 88, 99], [10, 20, 30]],
	[[12, 13, 14], [15, 16, 17]]
	]
	)
print(arr[0])
print(arr[1])
print(arr[2])

print(arr[0:1])
print(arr[:3])
print(arr[2, 0])

print(arr[2, 1, :2])
print(arr[2, 1, :-2])
print(arr[:, 1, 1])
print(arr[:, :2, 0])
print(arr[1, :, 2])

