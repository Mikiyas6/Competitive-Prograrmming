"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def BFS(root):
            queue = deque([root])
            while queue:
                level = len(queue)
                for i in range(level):
                    node = queue.popleft()
                    node.next = queue[0] if i < level - 1 else None
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return root
        
        return BFS(root)