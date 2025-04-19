class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        maxCount = 0
        maxIndex = 0
        for i in range(0, len(customers) - minutes + 1):
            currentCount = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    currentCount += customers[j]
            if currentCount > maxCount:
                maxCount = currentCount
                maxIndex = i

        for i in range(maxIndex, maxIndex + minutes):
            grumpy[i] = 0

        print(grumpy)

        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]

        return res