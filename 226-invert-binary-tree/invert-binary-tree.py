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
                return None
            inverted_left_side = invert(root.left)
            inverted_right_side = invert(root.right)
            root.left = inverted_right_side
            root.right = inverted_left_side
            return root
        return invert(root)