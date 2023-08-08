# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root,lists):
            if not root:
                return
            inorder(root.left,lists)
            lists.append(root.val)
            inorder(root.right,lists)
            return lists
        lists = []
        return inorder(root,lists)

        
