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
        def validate(root,minValue,maxValue):
            if not root:
                return True
            if minValue >= root.val or maxValue <= root.val:
                return False
            left = validate(root.left,minValue,root.val)
            right = validate(root.right,root.val,maxValue)
            return left and right
        
        return validate(root,minValue,maxValue)

            # if not root:
            #     return True
            # if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
            #     return False
            # left = validate(root.left)
            # right = validate(root.right)
            # return left and right
        
        return validate(root)
