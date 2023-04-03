# Queue is a FIFO Data Structure
# Queue() => Empty
# Queue.Enqueue(1,2,3)
# List looks 1,2,3
# Queue.Deque() => returns 1
# Queue.peek() => returns front of the Queue
class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, value) -> None:
        self.queue.append(value)

    def peek(self):
        if not self._is_empty():
            return self.queue[0]

    def dequeue(self):
        if not self._is_empty():
            return self.queue.pop(0)

    def _is_empty(self):
        return True if len(self.queue) == 0 else False

    def _len(self) -> int:
        return self.size()

    def size(self):
        return len(self.queue)
