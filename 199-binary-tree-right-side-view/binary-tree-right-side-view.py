# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def BFS(root):
            queue = deque([root])
            result = []
            while queue:
                level = len(queue)
                nodes = []
                for _ in range(level):
                    node = queue.popleft()
                    nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(nodes[-1])
            return result
        
        return BFS(root)