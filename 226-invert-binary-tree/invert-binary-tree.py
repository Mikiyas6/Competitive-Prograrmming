# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(root):

            if not root:
                return root
            
            temp = root.right
            root.right = invert(root.left)
            root.left = invert(temp)

            return root
        
        return invert(root)


