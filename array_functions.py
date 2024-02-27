from numpy import *

array1 = array([1, 2, 3, 4, 5, 6])
array2 = array([7, 8, 9, 10, 11, 23])
array3 = array1 + array2

print(array3)

# change structure of an array

arr = array([
    [1, 2, 3, 4, 5, 6],
    [11, 12, 13, 14, 15, 16]
])

arr2 = arr.flatten()
print(arr2)


arr3 = arr.reshape(3,2,2)
print(arr3)
print(array3)
print(sqrt(array3))