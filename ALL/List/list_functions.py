# APPEND(element) -> adds the element to the end of the list
# Works in O(1) CONSTANT time
a_list = [0, 1, 2, 3, 4, 5]
print(a_list)
a_list.append(6)
print(a_list)

# INSERT(index,element) -> adds the element before the index
# Works in O(N) LINEAR time due to the possibility of shifting elements in memory
a_list.insert(1, 0.5)
print(a_list)

# REMOVE(element) -> removes the element if in the list
# Works in O(N) LINEAR time due to the possbility of shifting elements in memory
# returns a runtime error if the index is out of bounds
a_list.remove(0.5)
print(a_list)

# POP(index) -> removes the element at the given index, if no index given removes the element at the end of the list
# works in O(1) CONSTANT time if the element POPPED is at the end of the list
# works in O(K) LINEAR/Kth time if the element is an intermediate index where k < n
# 'n' being the length of the list (*rememeber list like array values are zero based index)
print(a_list.pop())
a_list.pop(3)
print(a_list)
a_list.insert(3, 3)
print(a_list)

# REVERSE -> takes a list and reverses it
# works in O(N) Linear time
# this action occurs in-place
a_list.reverse()
print(a_list)
a_list.reverse()
print(a_list)

# SLICING -> you can use square brackets and a colon to define a range of elements within a list that you want to access or ‘slice’
# [index_beginning : up_to_ending_index_but_not_including]
# SLICING -> [beg_index : ending_index)
# [inclusive_index:exclusive_index]
print(a_list[1:len(a_list)-1])

# list[start:] means all numbers greater than start uptil the range
# 0 to end of list
print(a_list[0:])
# list[:end] means all numbers less than end uptil the range
# 0 to 3rd index in the list
print(a_list[:len(a_list)-2])
# list[:] means all numbers within the range
# all the elements in the list
print(a_list[:])

# STEPPED INDEXING -> Similiar to that of a FOR loop in other popular languages
# list[start:stop:step]
print(a_list[::2])
print(a_list[1::2])
# slicing indexes can also be negative
print(a_list[-1::-2])
print(a_list[-2::-2])

# Initializing new elements in a list
a_list[1:1] = list([0.25, 0.50, 0.75])
# the beginning index value is replaced, be careful about this!
print(a_list)


# Deleting -> using del keyword w/ slicing
# the del keyword is used to delete elements from a list.
# delete the numbers we just added
del a_list[1:4]
print(a_list)
a_list.append(6)
# delete all the even entries
del a_list[0::2]
print(a_list)
a_list.insert(0, 0)
a_list.insert(2, 2)
a_list.insert(4, 4)
a_list.append(6)
print(a_list)

# We can also use slicing techniques on strings since strings are lists of characters!
name = "Jonathan Yulan"
first_name = name[:8]
last_name = name[9:]
print(first_name, "is your first name and your last name is", last_name)
