# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            right = root.right
            left = root.left
            root.right = self.invertTree(left)
            root.left =  self.invertTree(right)

            return root

        else:
            return None