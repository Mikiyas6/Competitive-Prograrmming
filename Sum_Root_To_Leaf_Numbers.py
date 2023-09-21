# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calculate_sum(node, current_sum):
            if not node:
                return 0
            
            current_sum = current_sum * 10 + node.val
            
            if not node.left and not node.right:
                return current_sum
            
            return calculate_sum(node.left, current_sum) + calculate_sum(node.right, current_sum)
        
        return calculate_sum(root, 0)
