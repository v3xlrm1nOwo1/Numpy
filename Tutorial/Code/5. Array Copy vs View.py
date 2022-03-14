import numpy as np

"""
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
"""

# 1. Copy:
arr_1 = np.array([1, 2, 3, 4, 5])
copy = arr_1.copy()

print(f"Array: {arr_1} - Copy: {copy}")

arr_1[0] = 111
print(f"Array: {arr_1} - Copy: {copy}")

copy[0] = 222
print(f"Array: {arr_1} - Copy: {copy}")

# 2. View:

arr_2 = np.array([1, 2, 3, 4, 5])
view = arr_2.view()

print(f"Array: {arr_2} - Copy: {view}")

arr_2[0] = 111
print(f"Array: {arr_2} - Copy: {view}")

view[1] = 222
print(f"Array: {arr_2} - Copy: {view}")

# 3. Check if Array Owns its Data
"""
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object.
"""

print(f"Copy: {copy.base}")
print(f"View: {view.base}")