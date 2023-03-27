from double_linked_list import DLList


class MyQueue:
    """
    enqueue(element)	inserts element at the end of the queue
    dequeue()	        removes an element from the start of the queue
    front()	            returns the first element of the queue
    rear()	            returns the last element inserted into the queue
    isEmpty()	        checks if the queue is empty
    size()	            returns the size of the queue

    """

    def __init__(self):
        self.queue = DLList()

    def size(self):
        return self.queue.length

    def is_empty(self):
        return self.queue.is_empty()

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.queue.get_head()

    def rear(self):
        if self.is_empty():
            return None
        else:
            return self.queue.get_tail()

    def enqueue(self, element):
        self.queue.insert_at_tail(element)

    def dequeue(self):
        return self.queue.remove_head()

    def print_queue(self):
        return self.queue.dll_print()


q = MyQueue()
q.print_queue()
print("is_empty(): " + str(q.is_empty()))
print("rear(): " + str(q.rear()))
print("front(): " + str(q.front()))
print("size(): " + str(q.size()))
for i in range(0, 3):
    q.enqueue(i)
q.print_queue()
print("is_empty(): " + str(q.is_empty()))
print("rear(): " + str(q.rear()))
print("front(): " + str(q.front()))
print("size(): " + str(q.size()))
print("is_empty(): " + str(q.is_empty()))
print(q.dequeue())
print("rear(): " + str(q.rear()))
print("front(): " + str(q.front()))
print("size(): " + str(q.size()))
q.print_queue()
print(q.dequeue())
q.print_queue()
