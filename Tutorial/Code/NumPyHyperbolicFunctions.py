import numpy as np

# Hyperbolic Functions
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
a = np.pi/2

c = np.sinh(a)
print(f"Sinh {a}: {c}")

c = np.tanh(a)
print(f"Tanh {a}: {c}")

c = np.cosh(a)
print(f"Cosh {a}: {c}")


c = np.sinh(arr)
print(f"Sinh {arr}: {c}")

c = np.tanh(arr)
print(f"Tanh {arr}: {c}")

c = np.cosh(arr)
print(f"Cosh {arr}: {c}")

# Finding Angles

a = np.pi/2

arr = np.array([0.1, 0.2, 0.3])

c = np.arcsinh(a)
print(f"arcSinh {a}: {c}")

c = np.arctanh(a)
print(f"arcTanh {a}: {c}")

c = np.arccosh(a)
print(f"arcCosh {a}: {c}")


c = np.arcsinh(arr)
print(f"Sinh {arr}: {c}")

c = np.arctanh(arr)
print(f"Tanh {arr}: {c}")

c = np.arccosh(arr)
print(f"Cosh {arr}: {c}")
