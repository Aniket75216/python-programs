# Display array elements using slicing
import numpy as np

a = np.arange(1, 21)

print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate elements:", a[::2])
print("Reverse order:", a[::-1])
