# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.ans = False
        def helper(root,total):
            if not root:
                return
            if not root.left and not root.right:
                total += root.val
                self.ans = self.ans or total == targetSum
                return 
            total += root.val
            helper(root.left,total)
            helper(root.right,total)
        helper(root,0)
        return self.ans