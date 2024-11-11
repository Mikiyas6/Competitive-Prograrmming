# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        def BFS(root):
            queue = deque([root])
            result = []
            while queue:
                level = len(queue)
                total = 0
                for _ in range(level):
                    node = queue.popleft()
                    total += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(total/level)
            return result
        
        return BFS(root)
