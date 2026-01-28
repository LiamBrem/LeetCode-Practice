# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        adj = defaultdict(list) 
        leafNodes = set() 

        def iterate(curr):
            if not curr:
                return

            if curr.left:
                adj[curr].append(curr.left)
                adj[curr.left].append(curr)
                iterate(curr.left)

            if curr.right:
                adj[curr].append(curr.right)
                adj[curr.right].append(curr)
                iterate(curr.right)

            if not curr.left and not curr.right:
                leafNodes.add(curr)

            return

        iterate(root)

        res = 0
        path = set()

        def dfs(curr, currDist):
            nonlocal res
            if not curr or currDist > distance:
                return

            if currDist > 0 and curr in leafNodes and curr not in path:
                res += 1

            path.add(curr)

            for neighbor in adj[curr]:
                dfs(neighbor, currDist + 1) 


        for node in leafNodes:
            path = set()
            dfs(node, 0)
    
        return res // 2


        