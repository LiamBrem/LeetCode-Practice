# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parent = {}
        q = deque()
        q.append((root, 0))
        currLevelNodes = []
        currLevel = 0

        while q:
            curr, level = q.popleft()

            if level > currLevel:
                currLevel += 1
                currLevelNodes = [curr]
            else:
                currLevelNodes.append(curr)

            if curr.left:
                parent[curr.left] = curr
                q.append((curr.left, level + 1))
            if curr.right:
                parent[curr.right] = curr
                q.append((curr.right, level + 1))

        nodeSet = set(currLevelNodes)
        while len(nodeSet) > 1:
            nodeSet = set([parent[node] for node in nodeSet])

        return nodeSet.pop()
         
