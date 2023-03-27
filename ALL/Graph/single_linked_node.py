class LLNode:
    # Data is the value you want to store in the node. Think of it as the value at a specific index in a list. The data type can range from string or integer to a user-defined class.
    # The next pointer refers us to the next node in the list. It is essential for connectivity.
    def __init__(self, data=None, next=None):
        self.data = data  # data field
        self.next = next  # pointer to next node
