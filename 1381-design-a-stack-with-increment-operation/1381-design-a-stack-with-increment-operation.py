class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.max = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        if len(self.arr) < self.max:
            self.arr.append(x)
        
    def pop(self) -> int:
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i >= len(self.arr):
                break

            self.arr[i] += + val

        print(self.arr)  
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)