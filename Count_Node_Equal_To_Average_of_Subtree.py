# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def averageCalculator(root,lists):
            if not root.left and not root.right:
                lists.append(root.val)
                return lists
            if root.left and not root.right:
                lists = averageCalculator(root.left,lists)
                lists.append(root.val)
                return lists
            if not root.left and root.right:
                lists = averageCalculator(root.right,lists)
                lists.append(root.val)
                return lists
            else:
                lists = averageCalculator(root.left,lists)
                lists = averageCalculator(root.right,lists)
                lists.append(root.val)
                return lists
        def NodeCount(root,counter):
            if not root:
                return counter
            new_list = averageCalculator(root,[])
            average = sum(new_list)//len(new_list)
            if root.val == average:
                counter += 1
            counter = NodeCount(root.left,counter)
            counter = NodeCount(root.right,counter)
            return counter
        return NodeCount(root,0)
        
