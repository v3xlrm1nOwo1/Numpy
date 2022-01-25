import numpy as np

# 1- Create Ufunc
def add_num(x, y):
	return x + y

add_num = np.frompyfunc(add_num, 2, 1)

a = [1, 2, 3]
b = [4, 5, 6]

c = add_num(a, b)
print(c)

# 2- check if a function or ufunc
print(np.ufunc)

print(type(np.add))
print(type(add_num))

print(type(np.where))

