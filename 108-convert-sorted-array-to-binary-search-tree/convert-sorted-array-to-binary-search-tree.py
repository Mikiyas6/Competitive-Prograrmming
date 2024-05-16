# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(nums,s,e):

            if s > e:
                return None
            
            mid = s + (e-s)//2

            root = TreeNode(nums[mid])

            root.left = BST(nums,s,mid-1)

            root.right = BST(nums,mid+1,e)

            return root
        
        return BST(nums,0,len(nums)-1)



                

            



