class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total_sum = 0  

        def dfs(node):
            nonlocal total_sum  

            if not node:
                return 0

            if node.val % 2 == 0:  
                if node.left:
                    if node.left.left:
                        total_sum += node.left.left.val  
                    if node.left.right:
                        total_sum += node.left.right.val 
                if node.right:
                    if node.right.left:
                        total_sum += node.right.left.val  
                    if node.right.right:
                        total_sum += node.right.right.val 

            dfs(node.left)  
            dfs(node.right)  

        dfs(root)  
        return total_sum  
