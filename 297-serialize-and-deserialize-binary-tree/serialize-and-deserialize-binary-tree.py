# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root,string):

            if not root:
                return "N"

            return str(root.val) +","+ preorder(root.left,string)+"," + preorder(root.right,string)
        
        return preorder(root,"")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(",")
        data = data[::-1]

        def construct(data):

            if not data:
                return None
            
            if data[-1] == "N":
                data.pop()
                return None

            root = TreeNode(int(data.pop()))

            root.left = construct(data)

            root.right = construct(data)

            return root
        
        return construct(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))