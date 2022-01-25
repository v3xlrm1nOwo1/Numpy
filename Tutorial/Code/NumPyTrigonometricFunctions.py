import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
a = np.pi/2

c = np.sin(a)
print(f"Sin {a}: {c}")

c = np.tan(a)
print(f"Tan {a}: {c}")

c = np.cos(a)
print(f"Cos {a}: {c}")


c = np.sin(arr)
print(f"Sin {arr}: {c}")

c = np.tan(arr)
print(f"Tan {arr}: {c}")

c = np.cos(arr)
print(f"Cos {arr}: {c}")


# Convert Degrees Into Radians

c = np.deg2rad(a)
print(f"deg2rad {a}: {c}")

c = np.deg2rad(arr)
print(f"deg2rad {arr}: {c}")


# Radians to Degrees
a = 1.633123935319537e+16
arr = np.array([6.12323400e-17, 5.00000000e-01, 7.07106781e-01, 8.09016994e-01])

c = np.rad2deg(a)
print(f"rad2deg {a}: {c}")

c = np.rad2deg(arr)
print(f"rad2deg {arr}: {c}")

# Finding Angles
a = 1.0
arr = np.array([6.12323400e-17, 5.00000000e-01, 7.07106781e-01, 8.09016994e-01])

c = np.arcsin(a)
print(f"Sin {a}: {c}")

c = np.arctan(a)
print(f"Tan {a}: {c}")

c = np.arccos(a)
print(f"Cos {a}: {c}")


c = np.arcsin(arr)
print(f"Sin {arr}: {c}")

c = np.arctan(arr)
print(f"Tan {arr}: {c}")

c = np.arccos(arr)
print(f"Cos {arr}: {c}")

hypot = np.hypot(4, 5)
print(f"Hypot :{hypot}")