# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        visited = set()
        queue = deque([(target, 0)])  
        result = []
        
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                result.append(node.val)
            elif distance < k:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
        
        return result

        
