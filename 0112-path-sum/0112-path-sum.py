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
        
        def DFS(root,total,targetSum):
            if not root:
                return False
            if not root.left and not root.right:
                total += root.val
                if total == targetSum:
                    return True
                return False
            total += root.val
            left = DFS(root.left,total,targetSum)
            right = DFS(root.right,total,targetSum)
            return left or right
        
        return DFS(root,0,targetSum)
            