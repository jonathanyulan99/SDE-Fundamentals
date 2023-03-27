class MyStack:
    """
    push(element)       O(1)
    pop()               O(1)
    peek()              O(1)
    is_empty()          O(1)
    size()              O(1)
    """

    def __init__(self):
        self.stack_size = 0
        self.stack_list = []

    def is_empty(self):
        return self.stack_size == 0

    def get_size(self):
        return self.stack_size

    def peek(self):
        return self.stack_list[-1] if not self.is_empty() else None

    def push(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            return None
        LIFO = self.stack_list.pop()
        self.stack_size -= 1
        return LIFO

    def print(self):
        for x in reversed(self.stack_list):
            print(x)


myStack = MyStack()
print(myStack.peek())

for x in range(1, 10, 2):
    myStack.push(x)
print(f'Size of Stack: {myStack.get_size()}')
myStack.print()

print(f"Top Popped: {myStack.pop()}")
print(f"Top Popped: {myStack.pop()}")
myStack.print()
print(f'Size of Stack: {myStack.get_size()}')
