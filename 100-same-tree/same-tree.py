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
            if (not p and q) or (not q and p):
                return False
            if p.val != q.val:
                return False
            left = DFS(p.left,q.left)
            right = DFS(p.right,q.right)
            return left and right
        
        return DFS(p,q)
