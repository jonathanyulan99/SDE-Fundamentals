class LFUCache:
    class DLNode(object):
        def __init__(self, key=None, value=None, freq=0, next=None, prev=None):
            self.key = key
            self.value = value 
            self.freq = freq
            self.next = next 
            self.prev = prev 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {} 
        self.freq_nodes = {} # dictionary to hold nodes of same frequency
        self.head = LFUCache.DLNode(freq=float('inf'))
        self.tail = LFUCache.DLNode(freq=float('-inf'), prev=self.head) 
        self.head.next = self.tail 

    def get(self, key: int) -> int:
        node = self.key_node.get(key)
        if node is not None:
            # increment the frequency of the node
            node.freq += 1

            # move the node to the front of its frequency list
            curr_freq_list = self.freq_nodes[node.freq-1]
            curr_freq_list.remove(node)
            if not curr_freq_list:
                del self.freq_nodes[node.freq-1]
            if node.freq not in self.freq_nodes:
                self.freq_nodes[node.freq] = []
            next_freq_list = self.freq_nodes[node.freq]
            next_freq_list.append(node)

            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # if the key already exists, update the node value and frequency
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            node.freq += 1

            # move the node to the front of its frequency list
            curr_freq_list = self.freq_nodes[node.freq-1]
            curr_freq_list.remove(node)
            if not curr_freq_list:
                del self.freq_nodes[node.freq-1]
            if node.freq not in self.freq_nodes:
                self.freq_nodes[node.freq] = []
            next_freq_list = self.freq_nodes[node.freq]
            next_freq_list.append(node)
            return

        # if capacity is full, evict the least frequent node
        if len(self.key_node) == self.capacity:
            min_freq = min(self.freq_nodes)
            lru_node = self.freq_nodes[min_freq].pop(0)
            del self.key_node[lru_node.key]
            if not self.freq_nodes[min_freq]:
                del self.freq_nodes[min_freq]

        # create a new node and add it to the frequency list of 1
        node = LFUCache.DLNode(key=key, value=value, freq=1)
        if 1 not in self.freq_nodes:
            self.freq_nodes[1] = []
        freq_list = self.freq_nodes[1]
        freq_list.append(node)

        # add the node to the key_node dictionary
        self.key_node[key] = node
