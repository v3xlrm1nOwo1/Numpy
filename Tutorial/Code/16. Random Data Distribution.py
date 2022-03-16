import numpy as np



arr = np.random.choice([6, 8, 3, 1, 5], p=[0.0, 0.5, 0.2, 0.2, 0.1], size=(100))
print(arr)

arr = np.random.choice([6, 8, 3, 1, 5], p=[0.0, 0.5, 0.2, 0.2, 0.1], size=100)
print(arr)

arr = np.random.choice([6, 8, 3, 1, 5], p=[0.0, 0.5, 0.2, 0.2, 0.1], size=(5, 10))
print(arr)

