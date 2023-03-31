def power_of_three(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 3 == 0:
        return power_of_three(n/3)
    else:
        return False


print(*[x ** 3 for x in range(12)])
print(power_of_three(9999))


def power_of_x(n: int, x: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True

    if n % x == 0:
        return power_of_x(n/x, x)
    return False


class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_linked_list(list1: Node, list2: Node) -> Node:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.value < list2.value:
        list1.next = merge_linked_list(list1.next, list2)
        return list1
    list2.next = merge_linked_list(list1, list2.next)
    return list2


list1 = Node(1, Node(3, Node(5)))
list2 = Node(2, Node(4, Node(6, Node(7))))
list3 = merge_linked_list(list1, list2)

while list3:
    print(list3.value, end='-->')
    list3 = list3.next
print('None')
