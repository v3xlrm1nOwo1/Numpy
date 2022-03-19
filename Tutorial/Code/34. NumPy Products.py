import numpy as np



a = np.arange(1, 6)
b = np.arange(6, 11)
print(a, b)


# 1.
print(np.prod([a, b]))

# 2.
print(np.prod([a, b], axis=1))

# 3. 
print(np.prod([a, b], axis=0))

# 4.
print(np.cumprod(a))
print(np.cumprod(b))

