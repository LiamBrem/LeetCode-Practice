# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        if not root:
            return ""
            
        self.res = []

        def dfs(curr):
            if not curr:
                self.res.append("N")
                return

            self.res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)


        dfs(root)

        return ','.join(self.res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if data == "":
            return None

        self.res = data.split(',')
        self.i = 0

        def dfs():
            if self.res[self.i] == "N":
                self.i += 1
                return

            curr = TreeNode(self.res[self.i])

            self.i += 1
            curr.left = dfs()
            curr.right = dfs()

            return curr
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans