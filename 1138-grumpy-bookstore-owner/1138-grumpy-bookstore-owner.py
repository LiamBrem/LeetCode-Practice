class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        l = 0
        window = 0
        result = 0
        satisfied = 0
        maxWindow = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]
            
            if (r - l + 1) > minutes:
                if grumpy[l] == 1:
                    window -= customers[l]
                l += 1

            maxWindow = max(window, maxWindow)


        return satisfied + maxWindow