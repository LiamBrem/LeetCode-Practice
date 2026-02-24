class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFirst(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def removeLast(self):
        if self.tail.prev == self.head:
            return 
        
        node = self.tail.prev
        self.removeNode(node)
        return node
    
    def moveFirst(self, node):
        self.removeNode(node)
        self.addFirst(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {} # {key: node}
        self.ll = DLL() 

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            self.ll.moveFirst(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].val = value
            self.ll.moveFirst(self.m[key])

        else:
            self.m[key] = Node(key, value)
            self.ll.addFirst(self.m[key])
            if len(self.m) > self.capacity:
                removedNode = self.ll.removeLast().key
                del self.m[removedNode]

       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)