from collections import deque
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

        level_queue = deque([root])
        average_values = []

        while level_queue:
            level_size = len(level_queue)
            level_sum = 0

            for _ in range(level_size):
                current_node = level_queue.popleft()
                level_sum += current_node.val

                if current_node.left:
                    level_queue.append(current_node.left)
                if current_node.right:
                    level_queue.append(current_node.right)

            level_average = level_sum / level_size
            average_values.append(level_average)
        
        return average_values
