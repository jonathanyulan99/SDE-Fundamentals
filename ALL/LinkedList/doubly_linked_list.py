from doubly_linked_node import DLNode


class DLList:
    """
    The only difference between doubly and singly linked lists is that in DLLs each node contains pointers for both
    the previous and the next node. This makes the DLLs bi-directional.
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def get_head(self):
        if self.is_empty():
            return 'DLList is empty!'
        return self.head

    def get_tail(self):
        if self.is_empty():
            return 'DLList is empty!'
        return self.tail

    def is_empty(self):
        return True if not self.head else False

    def insert_at_head(self, inserted_value):
        inserted_node = DLNode(inserted_value, self.get_head(), None)
        self.head = inserted_node
        return self.head

    def insert_at_tail(self, inserted_value):
        if self.is_empty():
            inserted_node = DLNode(inserted_value)
            self.head = inserted_node
            self.tail = inserted_node
            return
        inserted_node = DLNode(inserted_value, None, self.get_tail())
        self.get_tail().next = inserted_node
        self.tail = inserted_node
        return

    def delete(self, searched_value):
        if self.is_empty():
            return "DLList is empty"
        head = self.get_head()

        if head.val == searched_value:
            self.head = self.get_head().next
            return
        while head.next.val != searched_value:
            head = head.next
        head.next = head.next.next
        return self.head

    def print(self):
        if self.is_empty():
            return "Self Is Empty"
        head = self.head

        while head.next:
            print(head, end=' -> ')
            head = head.next
        print(head, "-> None")


dll = DLList()
dll.insert_at_tail(99)
dll.print()
dll.delete(99)
dll.insert_at_head(2)
dll.print()
