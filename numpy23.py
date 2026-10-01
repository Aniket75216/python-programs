# Flatten a 3D array
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Original array:")
print(a)

print("Flattened array:")
print(a.flatten())
