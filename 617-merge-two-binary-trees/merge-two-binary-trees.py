# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS(root1,root2):

            if not root1 and not root2:
                return None
            
            if root1 and not root2:

                return root1
            
            if not root1 and root2:

                return root2

            root = TreeNode(root1.val + root2.val)
            
            root.left = DFS(root1.left,root2.left)

            root.right = DFS(root1.right,root2.right)

            return root 
        
        return DFS(root1,root2)

            