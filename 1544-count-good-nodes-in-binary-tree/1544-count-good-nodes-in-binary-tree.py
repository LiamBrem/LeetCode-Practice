# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
       
        def solve(root, maxNode):
            if not root:
                return
            
            if root.val >= maxNode:
                self.res += 1
                maxNode = root.val

            solve(root.left, maxNode)
            solve(root.right, maxNode)
        
        if not root:
            return 0
        
        solve(root, root.val)
        return self.res

                    
        