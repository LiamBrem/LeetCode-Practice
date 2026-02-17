# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Initially tried serializing like a heap
where position of child i = i * 2 + 1 and i *2 + 2
The issue with this is if the tree is sparse -> need a lot of memory for all the Null values

Instead doing a preorder traversal



""" 

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []

        def dfs(curr):
            if not curr:
                res.append("N")
                return

            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")[:-1]
        if len(arr) == 0 or arr[0] == 'N':
            return None

        self.i = 0
        root = TreeNode(arr[0])

        def dfs():
            if self.i >= len(arr) or arr[self.i] == "N":
                self.i += 1
                return None

            curr = TreeNode(int(arr[self.i]))
            self.i += 1
            curr.left = dfs()
            curr.right = dfs()


            return curr

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))