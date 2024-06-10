# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        sortedArray = []

        def inorder(root):

            if not root:
                return
            
            inorder(root.left)
            sortedArray.append(root.val)
            inorder(root.right)
        
        inorder(root)

        def BST(s,e):

            if s > e:
                return None
            
            mid = s + (e-s)//2

            newRoot = TreeNode(sortedArray[mid])

            newRoot.left = BST(s,mid-1)

            newRoot.right = BST(mid+1,e)

            return newRoot
        
        return BST(0,len(sortedArray)-1)