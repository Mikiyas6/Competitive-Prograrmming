# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        counter = 0
        def dfs(root,maxValue):
            nonlocal counter
            if not root:
                return
            maxValue = max(maxValue,root.val)
            if maxValue == root.val:
                counter += 1
            dfs(root.left,maxValue)
            dfs(root.right,maxValue)
        
        dfs(root,float('-inf'))
        return counter