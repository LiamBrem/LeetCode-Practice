class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {} # number : appearances

        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in values:
                values[num] += 1
            else:
                values[num] = 1

        for number, count in values.items():
            buckets[count].append(number)


        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result