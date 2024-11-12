# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        
        def DFS(root,count,k):
            nonlocal ans
            if not root:
                return count

            count = DFS(root.left,count,k) + 1
            if count == k:
                ans = root.val
            return DFS(root.right,count,k)
        
        DFS(root,0,k)
        return ans
