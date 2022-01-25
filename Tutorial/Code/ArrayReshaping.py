import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(f"1- Array: {arr}")

# ERROR 4 * 6 != 20
# re = arr.reshape(4, 6)
# print(f"Array: {re}")


re = arr.reshape(4, 5)
print(f"2- Array: {re}")

re = arr.reshape(5, 4)
print(f"3- Array: {re}")

re = arr.reshape(2, 2, 5, 1)
print(f"4- Array: {re}")

re = arr.reshape(2, 2, -1)
print(f"5- Array: {re}")

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(f"6- Array: {arr}")

re = arr.reshape(-1)
print(f"7- array: {re}")

print(f"8- Copy OR View: {re.base} Hmmmm (-_-) 'View'!!!")
