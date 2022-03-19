import numpy as np

x = [0, 1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
z = []

for i, j in zip(x, y):
	z.append(i + j)

print(z)

z = np.add(x, y)
print(z)


def my_add(a, b):
	return a + b


my_add = np.frompyfunc(my_add, 2, 1)

z = my_add(x, y)
print(z)

print(type(np.add))

print(type(np.concatenate))

print(type(my_add))

