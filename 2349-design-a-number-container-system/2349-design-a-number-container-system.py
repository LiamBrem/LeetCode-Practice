import heapq

class NumberContainers:
    def __init__(self):
        self.idxToNum = {} # {index: number that's there}
        self.numToIdx = {} # {number: [list of indices]}
    
    def change(self, index, number):
        if index in self.idxToNum and self.idxToNum[index] == number: 
            return

        self.idxToNum[index] = number

        if number not in self.numToIdx or not self.numToIdx[number]:
            self.numToIdx[number] = [index]
        else:
            heapq.heappush(self.numToIdx[number], index)
   
    def find(self, number):
        while number in self.numToIdx and len(self.numToIdx[number]) > 0:
            idx = self.numToIdx[number][0]
            if idx in self.idxToNum and self.idxToNum[idx] == number:
                return idx

            heapq.heappop(self.numToIdx[number])

        return -1



        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)