# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def BFS(root):
            queue = deque([root])
            value = root.val
            while queue:
                level = len(queue)
                for _ in range(level):
                    node = queue.popleft()
                    if node.val != value:
                        return False
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return True
        
        return BFS(root)