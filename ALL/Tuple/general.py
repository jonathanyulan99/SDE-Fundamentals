tuple_num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slicing
sliced_tuple_num = tuple_num[2:5]
print(sliced_tuple_num)
# [start:up_to_but_not_include:step]
print(sliced_tuple_num[::2])
# easy reversing syntax
print(sliced_tuple_num[::-1])

my_tuple = "Max", 28, "Boston"
# unpacking must be exact
name, age, city = my_tuple
# unpack multiple with * operator
tuple_num_2 = 1, 2, 3, 4, 5
i1, *i2, i3 = tuple_num_2
print(i1)
# converts to a list due to the * operator
print(i2)
print(i3)

print(tuple_num_2.count(1))
print(tuple_num_2.index(5))
print(tuple_num_2[4])
print(len(tuple_num_2))
