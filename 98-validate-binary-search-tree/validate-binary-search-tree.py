# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        result = []

        def store(value):
            
            nonlocal result
            result.append(value)

        def DFS(root):

            if not root:
                return
            
            DFS(root.left)
            store(root.val)
            DFS(root.right)

            return
        
        DFS(root)
        
        i, j = 0, 1

        while j < len(result):

            if result[j] <= result[i]:
                return False

            i += 1
            j += 1

        return True
    
        