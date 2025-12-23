class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []

        def dfs(i, curr):
            if i >= len(nums):
                if tuple(curr) not in seen:
                    res.append(curr)

                seen.add(tuple(curr))
                return

            dfs(i + 1, curr)
            dfs(i + 1, curr + [nums[i]])

        dfs(0, [])

        return res