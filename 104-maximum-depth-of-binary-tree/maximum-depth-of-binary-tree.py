# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def max_depth(root,depth):

            if not root:
                return depth
            
            left_depth = max_depth(root.left,depth+1)
            right_depth = max_depth(root.right,depth+1)

            return max(left_depth,right_depth)
        
        return max_depth(root,0)