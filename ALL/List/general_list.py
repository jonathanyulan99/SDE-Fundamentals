# In Python, a list is an ordered sequence of heterogeneous elements. In other words, a list can hold elements with different data types.

def foo() -> None:
    print("Hello from function foo!")


a_list = ['a', 'bcde', 'f']

another_list = ['c', 'string', a_list, foo, ["Another List!"]]

print(another_list[0])
print(another_list[1])
another_list[3]()
print(str(another_list[4][0])[0])
print(another_list[2][1][2:])
