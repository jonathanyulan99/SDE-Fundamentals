# An array is just an ordered sequence of homogeneous elements. In other words, an array can only hold elements of one datatype.
# Python arrays are basically just wrappers for C arrays. The type is constrained and specified at the time of creation.

# array is a special package in the python library
import array as arr
import numpy as np
import array

# array_name = array.array('type', [list])
# type f -> float
# type I -> unsigned integer
# type b -> signed integer
# differences between i,b,h,q...are the size of the integer values being used
new_array = array.array('d', [0, 1, 2, 3, 4, 5])
print(new_array)
new_list = list(range(6))
print(new_list)

# Type_Code   C_Type   Python_Type  Min Size in Byes
#   'c'     character       char        1
#   'b'     signed char     int         1
#   'B'     unsigned char   int         1
#   'i'     signed int      int         2
#   'I'     unsigned int    long        4
#   'l'    signed long      int         4
#   'L'     unsigned long   long        4
#   'f'     float           flaot       4
#   'd'     double          float       8

# Slicing is the same in arrays as a list
even_array = new_array[0::2]
print(even_array)
odd_array = new_array[1::2]
print(odd_array)

# ARRAYS ARE MUTABLE
new_array[len(new_array)+1:] = array.array('d', range(6, 11))
print(new_array)
# deleting the last element in the list
del new_array[len(new_array)-1:]
# del new_array[-1]
print(new_array)

# can append one value to the end of the array similiar to a list
new_array.append(10)
print(new_array)
# can also extend the list, by adding a list of values to the array
new_array.extend(list(range(11, 16)))
print(*new_array)

# You can concatenate two arrays using + operator
new_array_2 = array.array('d', [16, 17, 18, 19, 20])
new_array += new_array_2
print(new_array)
# You can delete values in a similiar fashion as list, let us delete the array we just concantenated
del new_array[16:]
print(new_array)

# use .remove(value) to remove the first iteration of the value found in the list
# use .pop(index) to remove the value that sits at that index; defaults to the end of the list to mimic the same behavior as a STACK

array_array = arr.array('b', [1, 2, 3])
numpy_array = np.array([1, 2, 3])
print(type(numpy_array), numpy_array)
print(type(array_array), array_array)
