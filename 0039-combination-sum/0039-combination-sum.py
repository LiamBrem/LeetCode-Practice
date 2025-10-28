class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(currSum, arr):
            if currSum > target:
               return    
            if currSum == target:
                arrSorted = sorted(arr)
                if arrSorted not in res:

                    res.append(arrSorted)
                return

            for num in candidates:
                currSum += num
                dfs(currSum, arr + [num])
                currSum -= num


        dfs(0, [])
 

        return res