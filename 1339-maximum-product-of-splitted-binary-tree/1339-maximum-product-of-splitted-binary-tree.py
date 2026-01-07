# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def update(curr):
            if not curr:
                return 0

            curr.val += update(curr.left) + update(curr.right)
            return curr.val
           
        total = update(root)
        maxProd = -float('inf')

        def dfs(curr):
            nonlocal maxProd
            if not curr:
                return


            maxProd = max(maxProd, (total - curr.val) * curr.val)
            dfs(curr.left)
            dfs(curr.right)
            
        dfs(root) 
        return maxProd % (10 ** 9 + 7)

        