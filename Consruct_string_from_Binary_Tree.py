# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not(root):
            return ' '

        string = str(root.val)
        left_subtree_str = self.tree2str(root.left)
        right_subtree_str = self.tree2str(root.right)

        if root.left and root.right:
            string += '(' + left_subtree_str + ")(" + right_subtree_str +')'
        elif root.right:
            string += "()(" + right_subtree_str + ")"
        elif root.left:
            string += "(" + left_subtree_str + ")"
        return string
