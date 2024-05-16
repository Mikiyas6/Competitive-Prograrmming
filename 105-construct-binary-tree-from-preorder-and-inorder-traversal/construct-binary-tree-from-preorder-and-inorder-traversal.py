# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def DFS(preorder,inorder):

            if not preorder or not inorder:
                return None

            # The first element in preorder is the root
            root = TreeNode(preorder[0])

            # Find the index of the root in inorder array
            mid = inorder.index(preorder[0])

            # Recursively build the left and right subtrees
            root.left = DFS(preorder[1:mid+1], inorder[:mid])
            root.right = DFS(preorder[mid+1:], inorder[mid+1:])

            return root
        
        return DFS(preorder,inorder)
