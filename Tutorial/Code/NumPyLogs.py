import numpy as np
import math


a = np.array([1, 2, 3, 4, 5])

# 1- Log at Base 2
c = np.log2(a)
print(f"Log at Base 2: {c}")

# 2- Log at Base 10
c = np.log10(c)
print(f"Log at Base 10: {c}")

# 3- Log at Base e
c = np.log(c)
print(f"Log at Base e: {c}")

# 4- Log at Any Base
log = np.frompyfunc(math.log, 2, 1)
c = log(a, 5)
print(f"Log at Any Base: {c}")

