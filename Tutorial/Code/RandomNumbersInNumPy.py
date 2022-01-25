import numpy as np

## 1- Create Random Number

# 1- Random Number Between 0 and 1
arr = np.random.rand()
print(f"1- Random Number: {arr}")

# 2- Random Number Between 0 and any Number
arr = np.random.randint(10)
print(f"2- Random Number: {arr}")

# 3- Choice Random Number from list, tuple,...
arr = np.random.choice([1, 2, 3, 4, 5])
print(f"3- Random Number: {arr}")

## 2- Crate Array 

# 1- 
arr = np.random.rand(5)
print(f"1- Array: {arr}")

arr = np.random.rand(2, 5)
print(f"2- Array: {arr}")

# 2- 
arr = np.random.randint(10, size=5)
print(f"3- Array: {arr}")

arr = np.random.randint(100, size=(2, 5))
print(f"4- Array: {arr}")

# 3- 
arr = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=5)
print(f"5- Array: {arr}")

arr = np.random.choice(np.random.randint(1000, size=100), size=(2, 5))
print(f"6- Array: {arr}")