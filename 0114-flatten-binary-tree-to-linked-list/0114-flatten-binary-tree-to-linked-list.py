# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def DFS(root):
            if not root:
                return None
            left_flatten = DFS(root.left)
            right_flatten = DFS(root.right)
            if left_flatten:
                current = left_flatten
                while current.right:
                    current = current.right
                current.right = right_flatten
                root.right = left_flatten
            root.left  = None
            return root
        DFS(root)
        



