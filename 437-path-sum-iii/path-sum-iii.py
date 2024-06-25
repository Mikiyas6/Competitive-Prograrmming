# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        hashmap = defaultdict(int)
        hashmap[0] = 1
        counter = 0
        
        def dfs(node, total):
            nonlocal counter
            if not node:
                return
            
            total += node.val
            
            if (total - targetSum) in hashmap:
                counter += hashmap[total - targetSum]
            
            hashmap[total] += 1
            
            dfs(node.left, total)
            dfs(node.right, total)
            
            hashmap[total] -= 1  # Revert the addition to hashmap[total]
        
        dfs(root, 0)
        
        return counter


            