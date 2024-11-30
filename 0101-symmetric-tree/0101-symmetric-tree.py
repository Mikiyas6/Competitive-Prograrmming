# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetryCheck(queue1,queue2):
            while queue1 and queue2:
                level = len(queue1)
                for _ in range(level):
                    node1 = queue1.popleft()
                    node2 = queue2.popleft()
                    if node1 and not node2 or node2 and not node1:
                        return False
                    if node1 and node2:
                        if node1.val != node2.val:
                            return False
                        queue1.append(node1.left)
                        queue1.append(node1.right)
                        queue2.append(node2.right)
                        queue2.append(node2.left)
            return True
        
        if not root or (not root.left and not root.right):
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        if root.left.val != root.right.val:
            return False
        queue1 = deque([root.left])
        queue2 = deque([root.right])
        return symmetryCheck(queue1,queue2)