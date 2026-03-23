class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        arr1 = nums[:n]
        arr2 = nums[n:]

        for i in range(n):
            arr.append(arr1[i])
            arr.append(arr2[i])

        return arr