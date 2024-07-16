# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False

        # Step 1: Find LCA
        lca = findLCA(root, startValue, destValue)
        
        # Step 2: Find path from LCA to startValue
        pathToStart = []
        findPath(lca, startValue, pathToStart)
        
        # Step 3: Find path from LCA to destValue
        pathToDest = []
        findPath(lca, destValue, pathToDest)
        
        # Convert path to start to 'U's
        pathToStart = ['U'] * len(pathToStart)
        
        # Step 4: Combine paths
        return ''.join(pathToStart) + ''.join(pathToDest)

