# Demonstrate fromfile()
from array import array

a = array('i', [10, 20, 30, 40])
with open('array_data.bin', 'wb') as f:
    a.tofile(f)
b = array('i')
with open('array_data.bin', 'rb') as f:
    b.fromfile(f, 4)
print('Array:', b)
