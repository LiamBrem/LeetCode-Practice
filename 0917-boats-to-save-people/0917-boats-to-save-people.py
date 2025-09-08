class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people = sorted(people)

        l = 0
        r = len(people) - 1
        total = 0

        while l <= r:
            if people[l] + people[r] > limit:
                total += 1
            else:
                total += 1
                l += 1
            r -= 1


        return total