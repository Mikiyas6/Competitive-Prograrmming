# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, path):
            if not node:
                return

            # Convert node value to character ('a' to 'z')
            char = chr(node.val + ord('a'))

            # Append character to the path
            path = char + path

            # If leaf node, update the smallest string found so far
            if not node.left and not node.right:
                nonlocal smallest
                if not smallest or path < smallest:
                    smallest = path

            # Continue DFS for left and right child nodes
            dfs(node.left, path)
            dfs(node.right, path)

        smallest = ''
        dfs(root, '')
        return smallest

    # Helper function to build a binary tree from a list
    def build_tree(nodes, index):
        if index >= len(nodes) or nodes[index] is None:
            return None
        node = TreeNode(nodes[index])
        node.left = build_tree(nodes, 2 * index + 1)
        node.right = build_tree(nodes, 2 * index + 2)
        return node