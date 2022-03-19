import numpy as np


arr = np.arange(1, 11)
print(arr)

# 1.
print(np.log2(arr))

# 2.
print(np.log10(arr))

# 3.
print(np.log(arr))

# 4.
from math import log
log = np.frompyfunc(log, 2, 1)

print(log(arr, 5))

