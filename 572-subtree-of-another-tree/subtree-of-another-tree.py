# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if root1 and not root2:
                return False
            left = isSame(root1.left,root2.left)
            right = isSame(root1.right,root2.right)
            return left and right and root1.val == root2.val
        
        def helper(root):
            if not root:
                return False
            if isSame(root,subRoot):
                return True
            left = helper(root.left)
            right = helper(root.right)
            return left or right
        return helper(root)