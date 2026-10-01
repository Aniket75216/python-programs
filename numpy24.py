# Calculate statistics after flattening a 3D array
import numpy as np

a = np.arange(1, 28).reshape(3, 3, 3)
flat = a.flatten()

print("Flattened array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
