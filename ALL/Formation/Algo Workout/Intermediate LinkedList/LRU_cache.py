'''
Q. Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class.

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Examples:
See test cases.
'''
class LRUCache(object):
    class DLNode(object):
        def __init__(self,value=0,prev=None,next=None):
            self.value = value 
            self.prev = prev 
            self.next = next
    
    def __init__(self):
        self.capacity = 3
        self.cache_dict = {} 
        self.head = LRUCache.DLNode(float('inf'))
        self.tail = LRUCache.DLNode(float('-inf'),prev=self.head)
        self.head.next = self.tail 
        self.length = 0 

    def get(self, key: int) -> int:
        return_value = self.cache_dict.get(key,None)
        if return_value:
            curr = self.head
            while curr.next != return_value:
                curr = curr.next 
            moved_node = curr.next 
            curr.next = curr.next.next 
            moved_node.next.prev = curr 
            moved_node.next = self.head.next
            moved_node.prev = self.head 
            self.head.next = moved_node
            curr = self.head 
            return return_value.value
        return return_value

    def put(self, key: int, val: int) -> int:
        inserted_node = LRUCache.DLNode(val)
        return_value = self.cache_dict.get(key, None)
        if return_value:
        # update the value for an existing key
            curr = self.head
            while curr.next != return_value:
                curr = curr.next
            moved_node = curr.next
            curr.next = curr.next.next
            moved_node.next.prev = curr
            moved_node.next = self.head.next
            moved_node.prev = self.head
            self.head.next = moved_node
            return return_value.value
        else:
            inserted_node = LRUCache.DLNode(val)
            if self.length > self.capacity:
                LRU_Node = self.tail.prev 
                LRU_Node.prev.next = self.tail
                self.tail.prev = LRU_Node.prev
                LRU_Node.next = None 
                LRU_Node.prev = None 
                for k,v in self.cache_dict.items:
                    if v == LRU_Node:
                        del self.cache_dict[k] 
                        break
                self.length-=1 
            inserted_node.prev = self.head 
            inserted_node.next = self.head.next 
            self.head.next.prev = inserted_node 
            self.head.next = inserted_node 
            self.cache_dict[key] = inserted_node
            return key 

# Test Cases
cache = LRUCache()
print(cache.get(0)) # None
cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
print(cache.get(1)) # 10
print(cache.get(2)) # 20
cache.put(4, 40)
print(cache.get(3)) # None because purged when 4 was put in.
print(cache.get(4))