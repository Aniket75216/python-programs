# Demonstrate tounicode()
from array import array

a = array('u', 'PYTHON')
print('Unicode string:', a.tounicode())
