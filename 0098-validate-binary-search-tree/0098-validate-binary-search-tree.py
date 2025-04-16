# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.allNodes = []
        self.isValid = True

        def getAllNodes(curr):
            if not curr:
                return
            
            self.allNodes.append(curr)
            getAllNodes(curr.left)
            getAllNodes(curr.right)


        def dfs(curr):
            if not curr:
                return
            
            if curr.right:
                self.allNodes.clear()
                getAllNodes(curr.right)
                
                for node in self.allNodes:
                    if node.val <= curr.val:
                        self.isValid = False

            if curr.left:
                self.allNodes.clear()
                getAllNodes(curr.left)
                for node in self.allNodes:
                    if node.val >= curr.val:
                        self.isValid = False

            dfs(curr.left)
            dfs(curr.right)


        dfs(root)
        return self.isValid
        