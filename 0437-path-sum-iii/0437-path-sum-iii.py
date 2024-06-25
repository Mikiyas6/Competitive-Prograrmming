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
        
        def dfs(root,total):

            nonlocal counter
            if not root:
                return

            total += root.val

            if hashmap[total-targetSum]:
                counter += hashmap[total-targetSum]

            hashmap[total] += 1

            dfs(root.left,total)
            dfs(root.right,total)
            
            hashmap[total] -= 1
        
        dfs(root,0)

        return counter


            