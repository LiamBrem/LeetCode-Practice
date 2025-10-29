class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(cur, i):
            
            if (i >= len(nums)):
                res.append(cur[:])
                return

            cur.append(nums[i])
            bt(cur, i + 1)  
            cur.pop()
            bt(cur, i + 1)


        bt([], 0)

        return res