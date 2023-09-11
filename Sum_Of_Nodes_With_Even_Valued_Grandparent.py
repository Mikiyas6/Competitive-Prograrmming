class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total_sum = 0  # Initialize a variable to keep track of the total sum of even-grandparent values.

        def dfs(node):
            nonlocal total_sum  # Use a more descriptive name for the total sum variable.

            if not node:
                return 0

            if node.val % 2 == 0:  # Check if the current node's value is even.
                if node.left:
                    if node.left.left:
                        total_sum += node.left.left.val  # Add the value of the left grandchild if it exists.
                    if node.left.right:
                        total_sum += node.left.right.val  # Add the value of the right grandchild if it exists.
                if node.right:
                    if node.right.left:
                        total_sum += node.right.left.val  # Add the value of the left grandchild if it exists.
                    if node.right.right:
                        total_sum += node.right.right.val  # Add the value of the right grandchild if it exists.

            dfs(node.left)  # Recursively explore the left subtree.
            dfs(node.right)  # Recursively explore the right subtree.

        dfs(root)  # Start the depth-first search from the root of the tree.
        return total_sum  # Return the computed total sum.
