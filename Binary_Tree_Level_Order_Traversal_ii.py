from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right

        if not root:
            return []

        level_queue = deque([root])
        all_items_by_level = []

        while level_queue:
            
            level_size = len(level_queue)
            level_items = []
            

            for _ in range(level_size):

                node = level_queue.popleft()
                level_items.append(node.val)

                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)

            all_items_by_level.append(level_items)

        return all_items_by_level[::-1]
