# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')

        def DFS(root):
            nonlocal ans
            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)
            total = 0
            if left > 0:
                total += left
            if right > 0:
                total += right
            ans = max(ans,total+root.val)
            result = root.val if max(left,right) < 0 else root.val + max(left,right)
            return result
        
        DFS(root)
        return ans