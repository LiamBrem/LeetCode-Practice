"""
Sort the arrays by times and go in order
Could have an array where each i = time s -> a lot of space if sparse
O(NlogN) with extra space (max time)

could have sorted array of tuples: (time, leader) and binary search to find time
where each time in the tuple is a unique time from times array
O(NlogN) where N is the length of times
"""
from collections import defaultdict
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        # iterate through arrays, updating state array at each time
        # keeping track of highest votes in a hashmap
        state = []
        leader = None
        votes = defaultdict(int)
        for i in range(len(times)):
            person, time = persons[i], times[i]
            votes[person] += 1
            if leader is None or votes[person] >= votes[leader]: 
                leader = person
            
            state.append((time, leader))

        self.state = state


    def q(self, t: int) -> int:
        # binary search
        arr = self.state
        l, r = 0, len(arr) -1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= t:
                l = mid + 1
            else:
                r = mid - 1

        return arr[r][1]

        

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)