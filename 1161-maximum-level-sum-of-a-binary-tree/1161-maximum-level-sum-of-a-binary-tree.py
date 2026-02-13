# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = defaultdict(int)

        def dfs(node, level):
            if not node:
                return

            sums[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        minLevel = float('inf')
        maxSum = float('-inf')

        for level in sums:
            if sums[level] > maxSum:
                minLevel = level
                maxSum = sums[level]
            elif sums[level] == maxSum:
                minLevel = min(minLevel, level)

        return minLevel

        