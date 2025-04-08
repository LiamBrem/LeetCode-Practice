# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while (curr.val > p.val and curr.val > q.val) or (curr.val < p.val and curr.val < q.val):
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr