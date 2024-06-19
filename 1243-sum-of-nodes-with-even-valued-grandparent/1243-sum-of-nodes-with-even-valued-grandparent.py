# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        total = 0

        def dfs(node,parent,Grandparent):
            
            nonlocal total
            
            if not node:
                return

            if Grandparent and Grandparent.val %2 == 0:
                total += node.val
            dfs(node.left,node,parent)
            dfs(node.right,node,parent)

        dfs(root,None,None)
        return total