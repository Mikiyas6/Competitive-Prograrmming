# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def DFS(root,p,q):

            if not root:
                return root
            if root == p or root == q:
                return root
        
            left = DFS(root.left,p,q)
            right = DFS(root.right,p,q)

            if left and right:
                return root
            
            if not right:
                return left
            
            return right
        
        return DFS(root,p,q)