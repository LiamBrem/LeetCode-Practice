class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value

        res = []
        while self.ptr < len(self.arr) and self.arr[self.ptr] != None:
            res.append(self.arr[self.ptr])
            self.ptr += 1

        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)