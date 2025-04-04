class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        seen = {}
        for pair in nums1:
            seen[pair[0]] = pair[1]

        for pair in nums2:
            if pair[0] in seen.keys():
                seen[pair[0]] += pair[1]
            else:
                seen[pair[0]] = pair[1]

        result = []
        for key, value in seen.items():
            result.append([key, value])

        return sorted(result)
