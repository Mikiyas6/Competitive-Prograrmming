# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root
        
        def DFS(root):
            if not root:
                return None
            left = DFS(root.left)
            right = DFS(root.right)
            root.left = right
            root.right = left
            return root
        
        return DFS(root)
