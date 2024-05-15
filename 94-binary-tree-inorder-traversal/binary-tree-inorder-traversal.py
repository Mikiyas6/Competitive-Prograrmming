# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def store(value):
            nonlocal result
            result.append(value)

        def inroder(root):

            if not root:
                return 
            
            inroder(root.left)
            store(root.val)
            inroder(root.right)

            return
        
        inroder(root)
        return result
