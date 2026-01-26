class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float('inf')
        arr.sort()
        res = []
        for i in range(len(arr) - 1):
            diff = abs(arr[i + 1] - arr[i])
            if diff < minDiff:
                minDiff = diff
                res = [[arr[i], arr[i + 1]]]

            elif diff == minDiff:
                res.append([arr[i], arr[i + 1]])
                
            
        return res

        