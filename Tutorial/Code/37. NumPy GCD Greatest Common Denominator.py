import numpy as np



a = 9
b = 12
c = 4

print(np.gcd(a, b))
print(np.gcd(b, c))
print(np.gcd(a, c))

arr = np.array([20, 56, 8, 10, 90])

print(np.gcd.reduce(arr))

