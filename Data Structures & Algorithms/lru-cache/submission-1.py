class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None # Double linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to nodes

        # Initialize double linked list starter nodes
        self.left = Node(0,0)
        self.right = Node(0,0)
        
        self.left.next = self.right # left = least recent
        self.right.prev = self.left # right = most recent

    # Some helper functions to remove and insert MRU
    def remove(self, node):
        prev, nxt = node.prev, node.next
        
        prev.next = node.next
        nxt.prev = node.prev

    # insert node at the right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val # .val because it returns node
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove the LRU
            lru = self.left.next
            self.remove(lru)
            
            del self.cache[lru.key] # Delete from dict/ hash 
