# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root,val):

            if not root:
                node = TreeNode(val)
                return node
            
            if val < root.val:
                root.left = insert(root.left,val)
            else:
                root.right = insert(root.right,val)
            
            return root
        
        return insert(root,val)