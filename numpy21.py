# Replace values greater than 50 in a random 3D array
import numpy as np

a = np.random.randint(1, 101, size=(2, 3, 4))

print("Original array:")
print(a)

a[a > 50] = 0

print("After replacement:")
print(a)
