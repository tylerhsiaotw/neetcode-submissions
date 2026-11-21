class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            node.val = value

            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

            self.insert(node)
            
            if len(self.cache) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
