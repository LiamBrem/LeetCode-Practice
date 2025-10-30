# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def insertRec(cur):
            if val > cur.val:
                if cur.right:
                    insertRec(cur.right)
                else:
                    cur.right = TreeNode(val)
                    return  
            elif val < cur.val:
                if cur.left:
                    insertRec(cur.left)
                else:
                    cur.left = TreeNode(val)
                    return

        insertRec(root)

        return root    
