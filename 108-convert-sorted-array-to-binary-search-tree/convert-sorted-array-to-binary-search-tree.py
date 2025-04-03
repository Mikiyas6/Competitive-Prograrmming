# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start,end,nums):
            if start > end:
                return None
            mid = start + (end-start)//2
            root = TreeNode(nums[mid])
            root.left = helper(start,mid-1,nums)
            root.right = helper(mid+1,end,nums)
            return root
        return helper(0,len(nums)-1,nums)