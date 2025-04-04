# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root,p,q):
            if not root:
                return None
            if root == p:
                return p
            if root == q:
                return q
            left = helper(root.left,p,q)
            right = helper(root.right,p,q)
            if not left and not right:
                return None
            if not left and right:
                return right
            if not right and left:
                return left
            return root
        return helper(root,p,q)