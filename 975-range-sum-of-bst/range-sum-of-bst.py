# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        def helper(root):
            if not root:
                return
            self.total += root.val if low <= root.val and root.val <= high else 0
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.total