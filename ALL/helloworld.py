def helloworld() -> None:
    print('Hello World!')


def helloworld2() -> None:
    print('Hello World <3')


x = helloworld
y = helloworld2

list_1 = list([x, y])

for function in list_1:
    function()

x = 1


def func():
    print(x)
   # x = 2


func()


def second_letter(word):
    return word[1]


names = ['AA', 'bb', 'BB', "aa", "ab", "ac", "ba", "cb", "ca"]
# this is the same as the following function using a callback function called sort on second letter
sorted_name = sorted(names, key=lambda x: x[1])
sorted_name2 = sorted(names, key=second_letter)
print(*sorted_name)
print(*sorted_name)

dic1 = {"Jonathan": 2, "Desiree": 1}
dic2 = dict(key2="Software", key3="Design")
print(dic1)
dic1_tuples = dic1.items()
print(dic1_tuples)
# returning the dic-view, which is really a list back into a dictionary
print(dict(dic1_tuples))
tuple1 = tuple([[1, 1], [1, 2], [1, 3]])
index_1_2 = tuple1.index([1, 2])
print(tuple1[index_1_2])
# this sorted function returns a list of whatever is called inside of it
tuple1_sorted = sorted(tuple1, key=second_letter, reverse=True)
print(tuple(tuple1_sorted))
