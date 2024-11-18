# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        minValue = float('-inf')
        maxValue = float('inf')

        def DFS(root,minValue,maxValue):
            
            if not root:
                return True
            if minValue < root.val and root.val < maxValue:
                left = DFS(root.left,minValue,root.val)
                right = DFS(root.right,root.val,maxValue)
                return left and right
            return False
        
        return DFS(root,minValue,maxValue)
