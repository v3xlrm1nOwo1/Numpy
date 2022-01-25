import numpy as np

a = np.array([1.4, 1.5, -1.4, -1.5])

# 1- Truncation and Fix
c = np.trunc(a)
print(f"Trunc: {c}")

c = np.fix(a)
print(f"Fix: {c}")

# 2- Rounding
c = np.around(a)
print(f"Round: {c}")

# 3- Floor
c = np.floor(a)
print(f"Floor: {c}")

# 4- Ceil
c = np.ceil(a)
print(f"Ceil: {c}")

