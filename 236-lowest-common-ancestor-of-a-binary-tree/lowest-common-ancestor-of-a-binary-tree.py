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
                return None

            if root.val == p.val or root.val == q.val:
                return root
            
            left = DFS(root.left,p,q)
            right = DFS(root.right,p,q)

            if not left:
                return right
            if not right:
                return left

            return root
        
        return DFS(root,p,q)
            
