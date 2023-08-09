# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root,lists):
            if not root:
                return
            inorder(root.left,lists)
            lists.append(root.val)
            inorder(root.right,lists)
            return lists
        lists = inorder(root,[])
        def helper(lists,left,right):
            if right == len(lists):
                return True
            if lists[left] < lists[right]:
                return helper(lists,left+1,right+1)
            return False
        return helper(lists,0,1)
        # def helper(root,boolean):
        #     if not root:
        #         return
        #     if boolean and root.left:
        #         if root.val > root.left.val:
        #             boolean = self.isValidBST(root.left)
        #         else:
        #             boolean = False
        #     if boolean and root.right:
        #         if root.right.val > root.val:
        #             boolean = self.isValidBST(root.right)
        #         else:
        #             boolean =  False
        #     return boolean
        # return helper(root,True)
            
