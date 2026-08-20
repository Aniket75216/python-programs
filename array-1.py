from array import array 
#1).append() method
arr=[1,2,3]
arr.append(4)
print(arr)

#2).buffer_info() method
arr=array("i",[55,66,77])
print(arr.buffer_info())

#byteswap() method
arr=array("i",[55,66,77])
arr.byteswap()
print(arr)

#count() method
arr=array("i",[55,66,77])
print(arr.count(55))

#extend method
arr1=array("i",[55,66,77])
arr2=array("i",[33,22,11])
arr1.extend(arr2)
print(arr1)

#frombytes method
arr2=array("i")
arr1=array("i",[5,6,7]).tobytes()
(arr2.frombytes(arr1))
print(arr2)
print(arr1)

a = Array([10, 20, 30])

a.fromlist([40, 50])
print(a.tolist())
# [10, 20, 30, 40, 50]

a.insert(2, 25)
print(a)
# [10, 20, 25, 30, 40, 50]

print(a.index(30))
# 3

print(a.pop())
# 50

a.remove(25)
a.reverse()

print(a.tolist())
# [40, 30, 20, 10]


