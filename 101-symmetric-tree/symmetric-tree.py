# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def BFS(root):

            if not root:
                return False
            
            queue = deque([root])
            
            while queue:

                level = len(queue)
                nodes = []

                for _ in range(level):

                    node = queue.popleft()

                    if not node:
                        nodes.append(None)
                    else:
                        nodes.append(node.val)

                        if node.left:
                            queue.append(node.left)
                        else:
                            queue.append(None)

                        if node.right:
                            queue.append(node.right)
                        else:
                            queue.append(None)
                
                i, j = 0, len(nodes)-1

                while i <= j:

                    if nodes[i] != nodes[j]:
                        return False
                    
                    i += 1
                    j -= 1
            
            return True
                        
        return BFS(root)