# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    
        level_queue = deque([root])
        average_values = []
        all_items_by_level = []

        while level_queue:
            
            level_size = len(level_queue)
            level_sum = 0
            level_items = []
            

            for _ in range(level_size):

                node = level_queue.popleft()
                level_items.append(node.val)
                level_sum += node.val

                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)

            all_items_by_level.append(level_items)
            level_average = level_sum / level_size
            average_values.append(level_average)

        return average_values
