# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, maxNode):
            if not curr:
                return
            
            if curr.val >= maxNode:
                self.res += 1
                maxNode = curr.val
            
            dfs(curr.left, maxNode)
            dfs(curr.right, maxNode)

        if not root:
            return 0
        
        dfs(root, root.val)
        return self.res
                    
        