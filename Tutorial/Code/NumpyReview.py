import numpy as np

# a = np.array([1, 2, 3, 4, 5], dtype='int16')

# print(a)

# print(a.itemsize) # 2byte > int16: 1byte = 8bet

# print(a.size) # Nembers of items array

# print(a.itemsize * a.size) # Totl Size of bytes

# print(a.nbytes) # Total Size of bytes



# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)

# print(b[0, 0, 0])
# b[0, 0, 0] = 0
# print(b)

# b[:, 1, :] = [[8,8], [9,9]]
# print(b)

# z = np.zeros((2, 5))
# print(z)

# o = np.ones((2, 5))
# print(o)

# f = np.full((2, 5), 95)
# print(f)

# f = np.full(b.shape, 95)
# print(f)

# fl = np.full_like(b, 77)
# print(fl)

# r = np.random.random_sample(b.shape)
# print(r) 

# i = np.identity(5) 
# print(i)

# r = np.repeat(b, 3, axis=0)
# print(r)

# a = np.array([1, 2, 3, 4, 5])
# print(a + 2) # a += 2
# print(a - 2) # a -= 2
# print(a / 2) # a /= 2
# print(a * 2) # a *= 2

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)

# a = np.array([1, 2, 3, 4, 5])
# print(np.min(a)) # axis=(0,1,-1,-2) in array > 1 dimantion
# print(np.max(a)) # axis=(0,1,-1,-2) in array > 1 dimantion

# print(a > 2)
# print(a%2 == 0)


# b = np.array([[[1, 2, 9], [3, 4, 9]], [[5, 6, 7], [8, 7, 8]]])
# print(b)

# print(np.any(b > 5, axis=1))
# print(np.all(b > 5, axis=1))
# print((b >= 5) & (b < 9)) # ~((b >= 5) & (b < 9))



# ## read data from file
# ## text = np.genfromtext('path.extation', delimiter=',')
# ## cv = np.loadtext('path.extaion', dtype='O', delimiter=',', unpack=True, skiprows=1)


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = np.linspace(0, 10, 100)
print(a)

a = np.arange(0, 100, 5)
print(a)

a = np.array(['Java', 'Jim', 'Jon', 'Luke'])
print(a)

search_J = np.vectorize(lambda s: s[0])(a) == 'J'

print(a[search_J])
l = lambda s: s[0]
print(l(a))
print(np.vectorize(a))

x = np.linspace(0, 10, 10001)
print(f"x: {x}")

y = np.exp(-x/10)*np.sin(x)
print(f"y: {y}")

# plt.plot(x, y)
# plt.show()


a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a.ravel())


