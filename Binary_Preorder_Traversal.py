# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,lists):
            if not root:
                return
            lists.append(root.val)
            preorder(root.left,lists)
            preorder(root.right,lists)
            return lists
        lists = []
        return preorder(root,lists)
