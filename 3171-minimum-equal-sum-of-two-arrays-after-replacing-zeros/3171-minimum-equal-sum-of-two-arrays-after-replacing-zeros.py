class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        arr1Sum = sum(x if x!= 0 else 1 for x in nums1)
        arr2Sum = sum(x if x!= 0 else 1 for x in nums2)

        arr1Zeros, arr2Zeros = nums1.count(0), nums2.count(0)

        if (arr1Zeros == 0 and arr2Sum > arr1Sum) or (arr2Zeros == 0 and arr1Sum > arr2Sum):
            return -1

        return max(arr1Sum, arr2Sum)
