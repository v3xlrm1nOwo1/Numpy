import numpy as np


rad = np.pi/2

arr_rad = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

### 1.

# 1.
print(np.sin(rad))
print(np.sin(arr_rad))

# 2.
print(np.cos(rad))
print(np.cos(arr_rad))

# 3.
print(np.tan(rad))
print(np.tan(arr_rad))


### 2.

# 1.
print(np.rad2deg(rad))
print(np.rad2deg(arr_rad))

# 2.
print(np.deg2rad(180))
print(np.deg2rad([360, 180, 90, 270]))

### 3.

# 1.
print(np.arcsin(1.0))
print(np.arcsin([1.0, 0.8660254, 0.70710678, 0.58778525]))

# 2. 
print(np.arccos(6.123233995736766e-17))
print(np.arccos([6.12323400e-17, 5.00000000e-01, 7.07106781e-01, 8.09016994e-01]))

# 3.
print(np.arctan(1.633123935319537e+16))
print(np.arctan([1.63312394e+16, 1.73205081e+00, 1.00000000e+00, 7.26542528e-01]))

###

base = 5
perp = 8

print(np.hypot(base, perp))

