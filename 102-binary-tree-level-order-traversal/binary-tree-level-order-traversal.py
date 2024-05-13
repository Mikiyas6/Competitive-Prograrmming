# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse(node, level):
            if not node:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        result = []
        traverse(root, 0)
        return result