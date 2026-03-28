"""
- use a doubly linked list
- Hash Map with TokenID: node for renewing
- generate -> add to head & remove expired
- countUnexpiredTokens -> remove expired by currentTime & return size



"""
class Node:
    def __init__(self, val=None, exp=None):
        self.val = val
        self.exp = exp
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def addHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def addTail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1
            
    def removeHead(self):
        if not self.head:
            return 
        
        if self.head == self.tail:
            ret = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return ret
            
        ret = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return ret
    
    def removeTail(self):
        if not self.tail:
            return
        if self.tail == self.head:
            ret = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return ret

        ret = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        self.size -= 1
        return ret

    def remove(self, node):
        if node == self.head:
            return self.removeHead()
        if node == self.tail:
            return self.removeTail()
    
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.index = {} # tokenId: node
        self.ll = DLL()

    def removeExp(self, currentTime):
        while self.ll.tail and self.ll.tail.exp <= currentTime:
            node = self.ll.removeTail()
            del self.index[node.val]


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.removeExp(currentTime)

        node = Node(tokenId, currentTime + self.ttl)
        self.index[tokenId] = node
        self.ll.addHead(node)
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.removeExp(currentTime)

        if tokenId not in self.index:
            return

        node = self.index[tokenId] 
        self.ll.remove(node)
        node.exp = currentTime + self.ttl
        self.ll.addHead(node)


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.removeExp(currentTime)
        return self.ll.size

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)