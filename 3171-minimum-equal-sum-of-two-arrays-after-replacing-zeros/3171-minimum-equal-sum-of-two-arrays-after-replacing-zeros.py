class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Find totals of both arrays 
        # Find number of zeroes for both arrays

        # Arr 1: 8
        # Arr 1, Zeroes: 2

        #Arr 2: 12
        # Arr 2, Zeroes: 1

        arr1Sum = sum(x if x!= 0 else 1 for x in nums1)
        arr2Sum = sum(x if x!= 0 else 1 for x in nums2)

        arr1Zeros, arr2Zeros = nums1.count(0), nums2.count(0)

        if (arr1Zeros == 0 and arr2Sum > arr1Sum) or (arr2Zeros == 0 and arr1Sum > arr2Sum):
            return -1

        return max(arr1Sum, arr2Sum)
