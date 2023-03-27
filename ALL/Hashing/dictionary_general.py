# Dictionary: Key-Value Pairs, Unordered, Mutable
my_dict = {}  # or dict()
my_dict_2 = {"name": "max", "age": 28, "city": "New York"}
print(my_dict_2)
my_dict = dict(name="Mary", age=27, city="Boston")
print(my_dict)

# accessing values
value_name = my_dict["name"]
# raises a key error if you don't have that key in the dictionary
value_age = my_dict["age"]

# mutable; can add to it
my_dict["email"] = "max@xyz.com"
# over ride the next key
my_dict["email"] = "coolmax@xyz.com"

# deleting
del my_dict["email"]
print(my_dict)
# removes the last inserted item
item = my_dict.popitem()
# can remove specific items too
item = my_dict.pop("age")
print(my_dict)

if "name" in my_dict:
    print(my_dict["name"])

try:
    print(my_dict["lastname"])
# catches the error here
except:
    print("error")

for key in my_dict_2:
    print(key, end=' ')
print()

for key in my_dict_2.keys():
    print(key, end=' ')
print()

for key, value in my_dict_2.items():
    print(key, value, end=' ')
print()

for value in my_dict_2.values():
    print(value, end=' ')
print()

my_dict_copy = my_dict_2  # DO NOT DO THIS
# DOING THE ABOVE will assign a pointer \
# that will make changes to the copy and the original dicitonary
my_dict_copy = my_dict_2.copy()
# also can use \
# my_dict_copy = dict(my_dict_2)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
value = my_dict[3]
print(value)
myTuple = 8, 7
# KEY MUST BE IMMUTABLE
# LIST CANNOT BE USED BECAUSE OF THEIR MUTABILITY
my_dict_2 = {myTuple: 15}
print(my_dict_2)
