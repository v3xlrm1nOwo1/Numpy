import numpy as np

"""
** Data Types in NumPy **
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

# 1.

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array(['A', 'B', 'C'])
print(arr.dtype)

arr = np.array([True, False, False, True])
print(arr.dtype)

arr = np.array([45j, 4+1j, 45j-6])
print(arr.dtype)


# 2. Checking the Data Type of an Array

arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(f"Array: {arr} - Type: arr.dtype")

arr = np.array(['A', 'B', 'C'], dtype=bool)
print(f"Array: {arr} - Type: {arr.dtype}")


# 3. Converting Data Type on Existing Arrays

arr = np.array([1, 2, 3, 4, 5])
new_arr = arr.astype('S')
print(f"Array: {new_arr} - Type: {new_arr.dtype}")

arr = np.array([True, False, False, True, True])
new_arr = arr.astype(int)
print(f"Array: {new_arr} - Type: {new_arr.dtype}")

# What if a Value Can Not Be Converted?
# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

