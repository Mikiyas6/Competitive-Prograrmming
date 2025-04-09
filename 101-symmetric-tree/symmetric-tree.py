# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            queue = deque([root])
            while queue:
                level = len(queue)
                nodes = []
                for _ in range(level):
                    node = queue.popleft()
                    if node:
                        nodes.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        nodes.append(None)
                left = 0
                right = len(nodes)-1
                while left <= right:
                    if nodes[left] != nodes[right]:
                        return False
                    left += 1
                    right -= 1
            return True
        return bfs(root)