# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # def accumulate(root,cumulative):

        #     if not root:
        #         return root
            
        #     root.val = root.val + cumulative

        #     root.left = accumulate(root.left,root.val)

        #     root.right = accumulate(root.right,root.val)

        #     return root
        
        # def find_node(root,target):

        #     if not root:
        #         return False
            
        #     if not root.left and not root.right and root.val == target:
        #         return True
            
        #     return find_node(root.left,target) or find_node(root.right,target)

        # root = accumulate(root,0)

        # return find_node(root,targetSum)

        def path_sum(root,cumulative,target):

            if not root:
                return False
            
            if not root.left and not root.right and root.val + cumulative == target:
                return True
            
            return path_sum(root.left,root.val+cumulative,target) or path_sum(root.right,root.val+cumulative,target)
        
        return path_sum(root,0,targetSum)