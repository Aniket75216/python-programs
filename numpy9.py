# Access rows, columns, diagonal and selected rows
import numpy as np

a = np.arange(1, 17).reshape(4, 4)

print("First row:", a[0])
print("Last column:", a[:, -1])
print("Diagonal:", np.diag(a))
print("Second and third rows:")
print(a[1:3])
