# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(root):
            queue = deque([root])
            hashmap = defaultdict(int)
            hashmap[root] = 0
            new_root = TreeNode(0)
            while queue:
                level = len(queue)
                total = 0
            # Finding the sum of the values of the below level
                for i in range(level):
                    node = queue[i]
                    if node.left:
                        total += node.left.val
                    if node.right:
                        total += node.right.val
            # For every node I pop on this level,
                # - I will append the left and right children if they exist to the queue
                # - I will calculate the sum of the values of the children if they exist
                # - Since I have the sum of all the values in the children's level, for these two children
                    # I will subtract their sum from the total and map each of them with this diff
                for _ in range(level):
                    node = queue.popleft()
                    local_total = 0
                    if node.left:
                        queue.append(node.left)
                        local_total += node.left.val
                    if node.right:
                        queue.append(node.right)
                        local_total += node.right.val
                    if node.left:
                        hashmap[node.left] = total-local_total
                    if node.right:
                        hashmap[node.right] = total-local_total
            return hashmap
        
        hashmap = bfs(root)

        # To create a new Tree based on the hashmap
        def dfs(root,hashmap):
            if not root:
                return None
            newRoot = TreeNode(hashmap[root])
            newRoot.left = dfs(root.left,hashmap)
            newRoot.right = dfs(root.right,hashmap)
            return newRoot
        
        return dfs(root,hashmap)
                
                    
                    
                

                    