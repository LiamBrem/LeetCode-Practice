# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while (p.val < curr.val and q.val < curr.val) or (p.val > curr.val and q.val > curr.val):
            if (p.val < curr.val and q.val < curr.val):
                curr = curr.left
            else:
                curr = curr.right

        return curr

        