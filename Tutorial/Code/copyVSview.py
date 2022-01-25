import numpy as np

# Copy
arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()

arr[0] = 10
copy[1] = 20

print(f"Array: {arr}")
print(f"Copy: {copy}")


# View
arr = np.array([1, 2, 3, 4, 5])
view = arr.view()

arr[0] = 10
view[1] = 20

print(f"Array: {arr}")
print(f"View: {view}")

# Copy VS View
print(f"Copy: {copy.base}")
print(f"View: {view.base}")