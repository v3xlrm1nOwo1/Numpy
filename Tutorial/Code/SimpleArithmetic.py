import numpy as np


a = np.array([9, 5, 6])
b = np.array([3, 4, 2])

# 1- Addition
c = np.add(a, b)
print(f"Addition: {c}")

# 2- Subtraction
c = np.subtract(a, b)
print(f"Subtraction: {c}")


# 3- Multiplication
c = np.multiply(a, b)
print(f"Multiplication: {c}")


# 4- Division
c = np.divide(a, b)
print(f"Division: {c}")


# 5- Remainder
c = np.mod(a, b)
print(f"Mod: {c}")

c = np.remainder(a, b)
print(f"Remainder: {c}")

# 6- Quotient and Mod
c = np.divmod(a, b)
print(f"Quotient and Mod: {c}")

# 7- Power
c = np.power(a, b)
print(f"Power: {c}")


# 8- Absolute Values
c = np.absolute(a, b)
print(f"Absolute Values: {c}")

