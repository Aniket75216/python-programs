# Calculate row-wise and column-wise sums
import numpy as np

a = np.arange(1, 17).reshape(4, 4)

print("Row sums:", np.sum(a, axis=1))
print("Column sums:", np.sum(a, axis=0))
