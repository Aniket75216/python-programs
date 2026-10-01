# Sort an array in ascending and descending order
import numpy as np

a = np.array([40, 10, 70, 20, 90, 30, 60, 50])

print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])
