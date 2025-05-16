# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(curr, k):
            if not curr:
                return
            dfs(curr.left, k)
            self.c += 1
            if self.c == k:
                self.res = curr.val
                return

            dfs(curr.right, k)

        self.res = 0
        self.c = 0

        dfs(root, k)
        
        return self.res
        


        