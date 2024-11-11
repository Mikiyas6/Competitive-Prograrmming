# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if not root:
            return False
        
        def BFS(root):
            queue = deque([root])
            hashmap = defaultdict(list)
            level = 0
            hashmap[root.val] = [level,None]
            level += 1
            while queue:
                num_of_nodes = len(queue)
                for _ in range(num_of_nodes):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                        hashmap[node.left.val] = [level,node.val]
                    if node.right:
                        queue.append(node.right)
                        hashmap[node.right.val] = [level,node.val]
                level += 1
            return hashmap
        
        hashmap = BFS(root)
        level1,parent1 = hashmap[x]
        level2,parent2 = hashmap[y]
        return level1 == level2 and parent1 != parent2
                