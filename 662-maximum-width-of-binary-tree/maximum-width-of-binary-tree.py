# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # Queue of pairs (node, position)
        
        while queue:
            level_length = len(queue)
            level_min = float('inf')
            level_max = float('-inf')
            
            for _ in range(level_length):
                node, pos = queue.popleft()
                level_min = min(level_min, pos)
                level_max = max(level_max, pos)
                
                if node.left:
                    queue.append((node.left, 2 * pos + 1))
                if node.right:
                    queue.append((node.right, 2 * pos + 2))
            
            max_width = max(max_width, level_max - level_min + 1)
        
        return max_width