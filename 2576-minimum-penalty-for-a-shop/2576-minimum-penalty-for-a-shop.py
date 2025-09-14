'''
input: string cusomers w/ chars 'N'/'Y'
output: earliest hour to close for minimum penalty

notes:
    - Y: customers come at ith hour
    - N: no customers at the ith hour
    - penalty += 1 shop open w/ no customers
    - penalty += 1 shop open & customers come
    - len(customers) at least 1


"Y Y N Y"

penalty: 2


process:
    - iterate through & find total penalty when closed @ 0
    - iterate through a second time:
    - for each value, if Y we decrease 1 from penalty, N=increment


'''


class Solution:
    def bestClosingTime(self, customers: str) -> int:


        minimumPenalty = 0

        # find the penalty of being closed at hour 0        
        for i in range(len(customers)):
            if customers[i] == 'Y':
                minimumPenalty += 1

        minimumPosition = 0
        currentPenalty = minimumPenalty
        for i in range(len(customers)):
            if customers[i] == 'Y':
                currentPenalty -= 1
            else:
                currentPenalty += 1

            if currentPenalty < minimumPenalty:
                minimumPenalty = currentPenalty
                minimumPosition = i + 1

        return minimumPosition
