class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            p1 = 0
            p2 = 0

            result = []
            while p1 < len(a) and p2 < len(b):
                if a[p1] < b[p2]:
                    result.append(a[p1])
                    p1 += 1
                else:
                    result.append(b[p2])
                    p2 += 1

            if p1 < len(a):
                result += a[p1:]
            if p2 < len(b):
                result += b[p2:]

            return result

        def sort(arr):
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2

            return merge(sort(arr[:mid]), sort(arr[mid:]))


        return sort(nums)
        