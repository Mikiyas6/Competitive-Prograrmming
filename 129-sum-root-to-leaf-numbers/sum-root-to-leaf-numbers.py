# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def DFS(root,result):
            if not root:
                return "0"
            if not root.left and not root.right:
                final_result = result+[str(root.val)]
                return ''.join(final_result)
            left = DFS(root.left,result+[str(root.val)])
            right = DFS(root.right,result+[str(root.val)])
            return int(left)+int(right)

        return int(DFS(root,[]))

