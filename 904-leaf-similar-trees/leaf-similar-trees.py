# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafCollector(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return leafCollector(root.left) + leafCollector(root.right)
        leaf1 = leafCollector(root1)
        leaf2 = leafCollector(root2)
        if len(leaf1) != len(leaf2):
            return False
        i, j = 0, 0
        while i < len(leaf1) and j < len(leaf2):
            if leaf1[i] != leaf2[j]:
                return False
            i += 1
            j += 1
        return True