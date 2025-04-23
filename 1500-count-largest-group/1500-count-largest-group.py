class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = {}

        for i in range(1, n + 1):
            num = i
            dsum = 0
            while num > 9:
                dsum += num % 10
                num //= 10
            dsum += num

            if dsum in sums:
                sums[dsum] += 1
            else:
                sums[dsum] = 1

        res = 0
        greatest = 0
        for num in sums:
            if sums[num] > greatest:
                res = 1
                greatest = sums[num]
            elif sums[num] == greatest:
                res += 1

        return res