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
                temp_queue = deque()

                for _ in range(level):

                    node = queue.popleft()
                    if queue:
                        node.next = queue[0]
                    else:
                        node.next = None

                    if node.left:
                        temp_queue.append(node.left)
                    if node.right:
                        temp_queue.append(node.right)
                
                queue = temp_queue

            return root
        
        return BFS(root)