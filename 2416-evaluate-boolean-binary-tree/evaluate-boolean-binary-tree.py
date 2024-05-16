# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(root):

            if not root.left and not root.right:
                if root.val == 1:
                    return True

                return False
            
            left_side_value = DFS(root.left)
            right_side_value = DFS(root.right)

            if root.val == 2:
                return left_side_value or right_side_value

            return left_side_value and right_side_value
        
        return DFS(root)

