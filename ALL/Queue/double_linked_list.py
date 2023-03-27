class DLNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return False if self.head else True

    def get_head(self):
        if self.is_empty():
            return False
        return self.head.value

    def get_tail(self):
        if self.is_empty():
            return False
        return self.tail.value

    def insert_at_head(self, value):
        value_node = DLNode(value)

        if self.is_empty():
            self.head, self.tail = value_node, value_node
        else:
            value_node.next = self.get_head()
            self.get_head = value_node
        return

    def insert_at_tail(self, value):
        value_node = DLNode(value)

        if self.is_empty():
            self.insert_at_head(value)
        else:
            self.tail.next = value_node
            value_node.prev = self.tail
            self.tail = value_node
        self.length += 1
        return value_node.value

    def remove_head(self):
        if self.is_empty():
            return False
        head = self.head
        # case for when there is only one element
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
            head.prev = None
            head.next = None
        self.length -= 1
        return head.value

    def dll_print(self):
        if self.is_empty():
            print("Empty!")
            return
        temp = self.head
        while temp:
            print(temp.value, end="<--")
            temp = temp.next
        print('\n')

    def __str__(self):
        val = ""
        if (self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.value) + ", "
        temp = temp.next

        while (temp.next):
            val = val + str(temp.value) + ", "
            temp = temp.next
        val = val + str(temp.value) + "]"
        return val
