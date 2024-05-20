# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def DFS(root,min_value,max_value):

            if not root:
                return max_value-min_value

            min_value = min(min_value,root.val)
            max_value = max(max_value,root.val)

            left = DFS(root.left,min_value,max_value)

            right = DFS(root.right,min_value,max_value)

            return max(left,right)

        return DFS(root,root.val,root.val)