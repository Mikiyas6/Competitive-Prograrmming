# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0  # Initialize the maximum depth.
        current_depth = 0  # Initialize the current depth.
        
        def dfs(node, depth=0):
            nonlocal max_depth  # Use nonlocal to modify the max_depth variable in the outer scope.
            depth += 1  # Increment the current depth.
            
            if not node:
                return
            
            if not node.children:
                max_depth = max(max_depth, depth)  # Update max_depth if we reached a leaf node.
                depth = 0  # Reset the current depth to 0.
            
            for child in node.children:
                dfs(child, depth)  # Recursively explore children nodes.
        
        dfs(root)  # Start the depth-first search from the root node.
        
        return max_depth  # Return the maximum depth found in the tree.
