# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def preorder(root,height):
            if not root:
                return height 
            left_height = preorder(root.left,height+1)
            right_height = preorder(root.right,height+1)
            return max(left_height,right_height)
        return preorder(root,0)
