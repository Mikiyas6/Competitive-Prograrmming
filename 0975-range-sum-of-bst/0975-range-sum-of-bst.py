# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def preorder(root,low,high):
            nonlocal result
            if not root:
                return 
            result += root.val if root.val >= low and root.val <= high else 0
            if low <= root.val:
                preorder(root.left,low,high)
            if high >= root.val:
                preorder(root.right,low,high)
        preorder(root,low,high)
        return result