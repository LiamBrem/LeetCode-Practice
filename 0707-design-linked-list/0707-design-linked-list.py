class MyLinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def getNodeAt(self, index: int):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        return self.getNodeAt(index).val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.Node(val)
        else:
            node = self.Node(val)
            node.next = self.head
            self.head = node

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.Node(val)
        else:
            last = self.getNodeAt(self.size - 1)
            last.next = self.Node(val)

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            prev = self.getNodeAt(index - 1)
            new = self.Node(val)
            new.next = prev.next
            prev.next = new

            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        elif index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next
            
        elif index == self.size - 1:
            node = self.getNodeAt(self.size - 2)
            node.next = None
        
        else:
            prev = self.getNodeAt(index - 1)
            prev.next = prev.next.next

        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)