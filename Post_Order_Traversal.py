# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root,lists):
            if not root:
                return
            postorder(root.left,lists)
            postorder(root.right,lists)
            lists.append(root.val)
            return lists
        lists = []
        return postorder(root,lists)
