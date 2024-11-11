# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def DFS(root,result):
            if not root:
                return result
            result = DFS(root.left,result)
            result.append(root.val)
            return DFS(root.right,result)
        
        return DFS(root,[])