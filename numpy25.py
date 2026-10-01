# Filter flattened random 3D array using conditions
import numpy as np

a = np.random.randint(1, 101, size=(3, 4, 5))
flat = a.flatten()
average = np.mean(flat)

print("Array:")
print(a)
print("Greater than 50:", flat[flat > 50])
print("Even numbers:", flat[flat % 2 == 0])
print("Less than average:", flat[flat < average])
