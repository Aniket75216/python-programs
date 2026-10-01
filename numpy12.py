# Replace values greater than 50 with zero
import numpy as np

a = np.array([20, 65, 45, 80, 35, 90, 55, 40, 75, 30])

a[a > 50] = 0

print("Array:", a)
