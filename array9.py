# Demonstrate fromunicode()
from array import array

a = array('u')
a.fromunicode('HELLO')
print('Array:', a)
print('String:', a.tounicode())
