class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways = 0
        self.memo = {}
        
        @lru_cache(None)
        def dfs(currSum, i):
            if (currSum, i) in self.memo:
                return self.memo[(currSum, i)]

            if i == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            
            add = dfs(currSum + nums[i], i + 1)
            sub = dfs(currSum - nums[i], i + 1)

            self.memo[(currSum, i)] = add + sub
            return add + sub

        
        return dfs(0, 0)
