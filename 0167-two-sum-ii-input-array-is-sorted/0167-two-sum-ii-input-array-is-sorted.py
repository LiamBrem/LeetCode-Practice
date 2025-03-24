class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while True:
            total = numbers[p1] + numbers[p2]
            if total == target:
                return [p1 + 1, p2 + 1]
            elif total < target:
                p1 += 1
            else:
                p2 -= 1
