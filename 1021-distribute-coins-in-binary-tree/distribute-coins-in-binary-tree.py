# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves = 0
    
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively solve for the left and right subtrees
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # Calculate the current node's excess coins
            current_excess = node.val - 1 + left_excess + right_excess
            
            # Add the absolute value of current excess to the moves
            self.moves += abs(current_excess)
            
            # Return the current excess to the parent node
            return current_excess
        
        dfs(root)
        return self.moves