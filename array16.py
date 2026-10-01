# Demonstrate tofile()
from array import array

a = array('i', [10, 20, 30, 40])
with open('array_output.bin', 'wb') as f:
    a.tofile(f)
print('Array written to array_output.bin')
