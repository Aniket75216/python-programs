# Demonstrate frombytes()
from array import array

a = array('i', [10, 20, 30])
data = a.tobytes()
b = array('i')
b.frombytes(data)
print('Array:', b)
