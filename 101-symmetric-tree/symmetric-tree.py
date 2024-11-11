# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        def BFS(left_queue,right_queue):

            while left_queue and right_queue:
                level = len(left_queue)
                for _ in range(level):
                    node1 = left_queue.popleft()
                    node2 = right_queue.popleft()
                    if not node1 and node2:
                        return False
                    if not node2 and node1:
                        return False
                    if not node1 and not node2:
                        continue
                    if node1.val != node2.val:
                        return False
                    
                    left_queue.append(node1.left)
                    left_queue.append(node1.right)
                    right_queue.append(node2.right)
                    right_queue.append(node2.left)

            return True

        return BFS(deque([root.left]),deque([root.right]))


