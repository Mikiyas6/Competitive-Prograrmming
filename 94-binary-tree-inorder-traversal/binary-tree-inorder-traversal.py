# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root,result):
            if not root:
                return result
            final = inorder(root.left,result)
            final.append(root.val)
            return inorder(root.right,final)
        
        return inorder(root,[])