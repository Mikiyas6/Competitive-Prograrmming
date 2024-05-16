# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def DFS(p,q):

            if not p and not q:
                return True
                
            if not p and q:
                return False
            
            if not q and p:
                return False
            
            
            return p.val == q.val and DFS(p.left,q.left) and DFS(p.right,q.right)
        
        return DFS(p,q)