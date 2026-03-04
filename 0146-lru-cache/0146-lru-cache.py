class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.val = val
            self.key = key
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None # add
        self.tail = None # remove
        self.m = {} # {key: node}

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        node = self.m[key]
        self.removeNode(node)
        self.addNode(node) 

        return node.val

    def addNode(self, node): # adds to head
        node.next = self.head
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node

        node.prev = None
        self.head = node

    def removeNode(self, node):
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        

    def put(self, key: int, value: int) -> None:
        if key in self.m: # remove old from list  
            self.removeNode(self.m[key])
            
        self.m[key] = self.Node(key, value)
        self.addNode(self.m[key])

        if len(self.m) > self.capacity:
            del self.m[self.tail.key]
            self.removeNode(self.tail)

            
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)