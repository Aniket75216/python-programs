# Demonstrate pop()
from array import array

a = array('i', [10, 20, 30, 40])
removed = a.pop()
print('Removed:', removed)
print('Array:', a)
