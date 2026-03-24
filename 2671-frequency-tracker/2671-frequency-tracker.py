class FrequencyTracker:
    def __init__(self):
        self.frequencies = defaultdict(set) # for tracking {frequency: numbers}
        self.numCount = defaultdict(int) # for tracking {number: appearances}

    def add(self, number: int) -> None:
        if number in self.numCount and number in self.frequencies[self.numCount[number]]:
            self.frequencies[self.numCount[number]].remove(number)

        self.numCount[number] += 1
        self.frequencies[self.numCount[number]].add(number)
       

    def deleteOne(self, number: int) -> None:
        if number in self.numCount and number in self.frequencies[self.numCount[number]]:
            self.frequencies[self.numCount[number]].remove(number)
            self.numCount[number] -= 1
            if self.numCount[number] > 0:
                self.frequencies[self.numCount[number]].add(number)
        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequencies and len(self.frequencies[frequency]) > 0:
            return True

        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)