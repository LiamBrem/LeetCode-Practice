# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(curr, level):
            if not curr:
                return
            

            if len(res) <= level:
                res.append([curr.val])
            else:
                res[level].append(curr.val)

            bfs(curr.left, level + 1)
            bfs(curr.right, level + 1)


        bfs(root, 0)
        return(res)


