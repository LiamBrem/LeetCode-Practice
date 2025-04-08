# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True

        def isSame(t1, t2):
            if not t1 and not t2:
                return None
            elif (t1 and not t2) or (t2 and not t1):
                self.result = False
                return None
            elif t1.val != t2.val:
                self.result = False
                return None

            isSame(t1.left, t2.left)
            isSame(t1.right, t2.right)

        isSame(p, q)
        return self.result
