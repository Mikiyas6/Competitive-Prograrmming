# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        def bfs(root):

            queue = deque([root])
            all_items_by_level = []
            visited = set()
            i = 1

            while queue:

                level_items = []
                level_size = len(queue)
                
                for _ in range(level_size):

                    node = queue.popleft()
                    
                    if node not in visited:
                        level_items.append(node.val)
                        visited.add(node)
                    
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                
                if i %2 == 0:
                    all_items_by_level.append(level_items[::-1])
                else:
                    all_items_by_level.append(level_items)
                
                i += 1
            
            return all_items_by_level

        return bfs(root)


                    


                


