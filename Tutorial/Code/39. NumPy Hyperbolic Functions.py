import numpy as np


rad = np.pi/2

arr_rad = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

###

# 1.
print(np.sinh(rad))
print(np.sinh(arr_rad))

# 2.
print(np.cosh(rad))
print(np.cosh(arr_rad))

# 3.
print(np.tanh(rad))
print(np.tanh(arr_rad))

###

# 1.
print(np.arcsinh(2.3012989023072947))
print(np.arcsinh([2.3012989, 1.24936705, 0.86867096, 0.670484]))

# 2.
print(np.arccosh(2.5091784786580567))
print(np.arccosh([2.50917848, 1.60028686, 1.32460909, 1.20397209]))


# 3.
print(np.arctanh(0.9171523356672744))
print(np.arctanh([0.91715234, 0.78071444, 0.6557942, 0.55689331]))

