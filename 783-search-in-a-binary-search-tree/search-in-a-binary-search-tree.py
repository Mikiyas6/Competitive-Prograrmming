# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def BST(root,val):

            if not root or root.val == val:
                return root
            
            if val < root.val:
                return BST(root.left,val)
            else:
                return BST(root.right,val)
        
        return BST(root,val)