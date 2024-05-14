# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        def BFS(root):

            queue = deque([root])
            result = []

            while queue:

                level = len(queue)
                all_nodes_on_that_level = []

                for _ in range(level):

                    node = queue.popleft()
                    all_nodes_on_that_level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                if result:
                    result = [all_nodes_on_that_level] + result
                else:
                    result.append(all_nodes_on_that_level)
            
            return result

        return BFS(root)