# Separate even and odd numbers using Boolean indexing
import numpy as np

a = np.arange(1, 21)

print("Even numbers:", a[a % 2 == 0])
print("Odd numbers:", a[a % 2 != 0])
