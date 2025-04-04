# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        i = 0
        while queue:
            level = len(queue)
            if i %2 != 0:
                left, right = 0, level-1
                while left < right:
                    queue[left].val, queue[right].val = queue[right].val, queue[left].val
                    left += 1
                    right -= 1
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            i += 1
        return root
                

                