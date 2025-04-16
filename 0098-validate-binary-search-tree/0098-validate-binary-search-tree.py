# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, mn, mx):
            if not root:
                return True
            if mn != None and root.val <= mn.val:
                return False
            elif mx != None and root.val >= mx.val:
                return False
            
            return isValid(root.left, mn, root) and isValid(root.right, root, mx)


        return isValid(root, None, None)