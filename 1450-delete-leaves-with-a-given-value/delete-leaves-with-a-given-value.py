# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        # Recursively delete in left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current root is a leaf and its value is the target, delete it
        if not root.left and not root.right and root.val == target:
            return None
        
        return root