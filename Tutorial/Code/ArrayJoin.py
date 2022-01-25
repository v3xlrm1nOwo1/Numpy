import numpy as np

# Joining Arrays Using concatenate Functions
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.concatenate((a, b)) # a and b they have 1 dimansion beyt default axis=0
print(f"1- Array: \n{c}")

a = np.array([[1, 2, 3, 4], 
			  [5, 6, 7, 8]])

b = np.array([[9, 10, 11, 12], 
			  [13, 14, 15, 16]])

c = np.concatenate((a, b)) # defauld axis = 0 = -1
print(f"2 A- Array: \n{c}")

c = np.concatenate((a, b), axis=0) # defauld axis = 0 = -1
print(f"2 B- Array: \n{c}")

c = np.concatenate((a, b), axis=1) # axis = 1 = -1
print(f"3- Array: \n{c}")

a = np.array([[[1, 2, 3, 4, 5], 
			   [6, 7, 8, 9, 10]],

			  [[11, 12, 13, 14, 15], 
			   [16, 17, 18, 19, 20]]])

b = np.array([[[21, 22, 23, 24, 25], 
	               [26, 27, 28, 29, 30]], 

			      [[31, 32, 33, 34, 35], 
			       [36, 37, 38, 39, 40]]])

c = np.concatenate((a, b), axis=0) # defauld axis = 0 = -1
print(f"4- Array: \n{c}")

c = np.concatenate((a, b), axis=1) # axis 1 = -2
print(f"5- Array: \n{c}")


# Joining Arrays Using stack Functions
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.stack((a, b)) # a and b they have 2 dimansion beyt default axis=0
print(f"6- Array: \n{c}")

c = np.stack((a, b), axis=1)
print(f"7- Array: \n{c}")

a = np.array([[1, 2, 3, 4], 
			  [5, 6, 7, 8]])

b = np.array([[9, 10, 11, 12], 
			  [13, 14, 15, 16]])

c = np.stack((a, b), axis=0)
print(f"8- Array: \n{c}")

c = np.stack((a, b), axis=1)
print(f"9- Array: \n{c}")

a = np.array([[[1, 2, 3, 4, 5], 
			   [6, 7, 8, 9, 10]],

			  [[11, 12, 13, 14, 15], 
			   [16, 17, 18, 19, 20]]])

b = np.array([[[21, 22, 23, 24, 25], 
	               [26, 27, 28, 29, 30]], 

			      [[31, 32, 33, 34, 35], 
			       [36, 37, 38, 39, 40]]])

c = np.stack((a, b), axis=0)
print(f"10- Array: \n{c}")

c = np.stack((a, b), axis=1)
print(f"11- Array: \n{c}")



# Joining Arrays Using hstack - vstack - dstack Functions
c = np.hstack((a, b)) # hstack == concatenate with axis=1
print(f"12- Array: \n{c}")

c = np.vstack((a, b)) # hstack == concatenate with axis=0
print(f"13- Array: \n{c}")

c = np.dstack((a, b))
print(f"14- Array: \n{c}")


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.hstack((a, b)) # hstack == concatenate with axis=1
print(f"15- Array: \n{c}")

c = np.vstack((a, b)) # hstack == concatenate with axis=0
print(f"16- Array: \n{c}")

c = np.dstack((a, b))
print(f"17- Array: \n{c}")

