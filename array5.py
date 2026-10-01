# Demonstrate extend()
from array import array

a = array('i', [10, 20, 30])
a.extend(array('i', [40, 50]))
print('Array after extend:', a)
