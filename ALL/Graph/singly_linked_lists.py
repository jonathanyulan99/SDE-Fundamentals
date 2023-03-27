'''

Operation             LinkedList              List/Array
Access                  O(N)                   O(1)
Insert at Head          O(1)                   O(N)
Insert at Tail          O(N)                 O(N)/O(1)
Delete at Head          O(1)                   O(N)
Delete at Tail          O(N)                 O(N)/O(1)


'''
from single_linked_node import LLNode


class LinkedList:
    '''
    get_head() - returns the head of the list
    insert_at_tail(data) - inserts an element at the end of the linked list
    insert_at_head(data) - inserts an element at the start/head of the linked list
    delete(data) - deletes an element with your specified value from the linked list
    delete_at_head() - deletes the first element of the list
    search(data) - searches for an element with the specified value in the linked list
    is_empty() - returns true if the linked list is empty
    '''
    # The linked list itself is a collection of Node objects

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        # Ternary Operator: if_true_executed if condition else if_false_executed
        return True if not self.head else False

    def insert_at_head(self, data):
        data = LLNode(data)
        data.next = self.head
        self.head = data
        return self.head

    def insert_at_tail(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return self.head
        else:
            head = self.get_head()
            while head.next:
                head = head.next
            data = LLNode(data)
            head.next = data
            return self.head

    def print_list(self):
        if (self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, "-> None")
        return True

    def search(self, value):
        if self.is_empty():
            return False
        head = self.get_head()
        while head:
            if head.data == value:
                return True
            else:
                head = head.next

        return False

    def search_recursively(self, head, value):
        if not head:
            return False
        if head.data == value:
            return True
        return self.search_recursively(head.next, value)

    def delete_at_head(self):
        if self.is_empty():
            return
        head = self.get_head()
        self.head = head.next
        return

    def delete_by_value(self, value) -> None:
        if self.is_empty():
            return

        head = self.get_head()

        while head.next:
            if head.next.data == value:
                print(f"Deleted {head.next.data}")
                head.next = head.next.next
                return
            head = head.next

        print(f"Value {value} Not in List")
