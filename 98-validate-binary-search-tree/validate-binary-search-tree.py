# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        min_val=float('-inf')
        max_val=float('inf')
        
        def validate(root,min_val,max_val):

            if not root:
                return True
        
            # Check if the current root's value is within the valid range
            if not (min_val < root.val < max_val):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(root.left, min_val, root.val) and
                    validate(root.right, root.val, max_val))
        
        return validate(root,min_val,max_val)

        # result = []

        # def store(value):
            
        #     nonlocal result
        #     result.append(value)

        # def DFS(root):

        #     if not root:
        #         return
            
        #     DFS(root.left)
        #     store(root.val)
        #     DFS(root.right)

        #     return
        
        # DFS(root)
        
        # i, j = 0, 1

        # while j < len(result):

        #     if result[j] <= result[i]:
        #         return False

        #     i += 1
        #     j += 1

        # return True
    
        