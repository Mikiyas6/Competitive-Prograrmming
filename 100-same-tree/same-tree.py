# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p,q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            left = helper(p.left,q.left)
            if not left:
                return False
            right = helper(p.right,q.right)
            return left and right and p.val == q.val
        
        return helper(p,q)