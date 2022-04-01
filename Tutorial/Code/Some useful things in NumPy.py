import numpy as np


# 1. Zeros Array
arr = np.zeros(10)
print(arr)

arr = np.zeros((2, 5))
print(arr)

# 2. Ones Array
arr = np.ones(5)
print(arr)

arr = np.ones([2, 5])
print(arr)

# 3. Empty Array
arr = np.empty(10)
print(arr)

arr = np.empty((2, 5))
print(arr)

arr = np.eye(3, 2)
print(arr)

# 4. full array
arr = np.full(5, 8)
print(arr)

arr = np.full(5, arr)
print(arr)

# 5. (zeros, ones, empty, full) Like
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

arr = np.zeros_like(a)
print(arr)

arr = np.ones_like(a)
print(arr)

arr = np.empty_like(a)
print(arr)

arr = np.full_like(a, 5)
print(arr)


# 1. arange
arr = np.arange(0, 20, 3)
print(arr)

# 2. linspace
arr = np.linspace(0.0, 1.0, 10)
print(arr)



arr = np.random.uniform(0, 10, 5)
print(arr)

arr = np.random.randn(5)
print(arr)

arr = np.random.normal(0, 10, 5)
print(arr)

arr = np.arange(0, 21)
print(arr)

print(arr > 10)

print(np.any(arr > 10))

print(np.all(arr > 10))

print(arr[arr == 10])

print(arr[arr % 2 == 0])

print(arr[arr % 2 != 0])

## & = and, | = or, ^ = xor, ~ = not
print(arr[(arr % 2 == 0) & (arr > 10)])

a = np.arange(5)
b = np.arange(5, 10)
print(a, b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

arr = np.array([1, 3, 5, 67, 89])
print(arr)

### arr.fun()
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.var(arr))
print(np.argmax(arr))
print(np.argmin(arr))
print(np.mean(arr))
print(np.std(arr))


print(np.allclose(0.1 + 0.2, 0.3))
print(np.allclose(1e-9, 2e-9))
print(np.allclose(0.1 + 0.2 - 0.3, 0))


arr = np.array([
	[2, 4, 6],
	[7, 9, 4],
	[9, 1, 5]
	])
print(np.transpose(arr))

print(np.tile(arr, (1, 2)))
print(np.repeat(arr, 3, axis=1))
print(np.delete(arr, 1, axis=0))

print(np.eye(4))
print(np.diag([1, 2, 3]))
arr = np.array([[1, 2], [3, 4]])
print(np.diag(arr))
print(np.vander([1, 2, 3, 4], 3))


# Other than that, NumPy arrays are:
# more compact, especially when there’s more than one dimension
# faster than lists when the operation can be vectorized
# slower than lists when you append elements to the end
# usually homogeneous: can only work fast with elements of one type



rng  = np.random.default_rng()

# python list
l = [0, 1, 2]
a = l 		   # no copy
b = l[:]     # copy
c = l.copy() # copy
# numpy array
l = np.array([0, 1, 2])
a = l 		   # no copy
b = l[:]     # no copy
c = l.copy() # copy


np.var(arr, axis=None)
np.std(arr, axis=None, ddof=1.5)
np.mean(arr, axis=None)
np


np.sort(arr)
arr.sort()

