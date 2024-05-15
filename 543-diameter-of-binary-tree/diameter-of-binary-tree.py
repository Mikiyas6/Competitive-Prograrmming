# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = 0

        def store(diameter):

            nonlocal max_diameter

            max_diameter = max(max_diameter,diameter)
        
        def fun(root):

            if not root:
                return -1

            left_height = fun(root.left)
            right_height = fun(root.right)

            diameter = left_height + right_height + 2

            store(diameter)

            return max(left_height,right_height) + 1

        height = fun(root)

        return max_diameter