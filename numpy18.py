# Create and display a 3D array
import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
