class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        else:
            self.positions[val] = len(self.arr) 
            self.arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.positions:
            toMoveTo = self.positions[val]
            del self.positions[val]
            if len(self.arr) > 1:
                if toMoveTo != len(self.arr) -1:
                    moveVal = self.arr.pop()
                    self.arr[toMoveTo] = moveVal
                    self.positions[moveVal] = toMoveTo
                else:
                    self.arr = self.arr[:len(self.arr) - 1]
            else:
                self.arr = []
            return True
        
        else:
            return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()