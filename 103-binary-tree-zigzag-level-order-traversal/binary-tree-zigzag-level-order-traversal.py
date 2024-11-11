# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        def BFS(root):
            queue = deque([root])
            result = []
            flag = True
            while queue:
                level = len(queue)
                nodes = []
                for _ in range(level):
                    if flag:
                        node = queue.popleft()
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                    else:
                        node = queue.pop()
                        if node.right:
                            queue.appendleft(node.right)
                        if node.left:
                            queue.appendleft(node.left)
                    nodes.append(node.val)
                result.append(nodes)
                flag = not flag
            return result
        
        return BFS(root)
