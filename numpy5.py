# Reshape an array into different matrices
import numpy as np

a = np.arange(1, 13)

print("2 x 6:")
print(a.reshape(2, 6))

print("3 x 4:")
print(a.reshape(3, 4))

print("4 x 3:")
print(a.reshape(4, 3))
