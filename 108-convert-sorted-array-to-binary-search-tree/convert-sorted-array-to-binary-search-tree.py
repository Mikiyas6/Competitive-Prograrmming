# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def DFS(start,end,nums):
            if start > end:
                return None
            mid = start + (end-start)//2
            root = TreeNode(nums[mid])
            root.left = DFS(start,mid-1,nums)
            root.right = DFS(mid+1,end,nums)
            return root
        
        start = 0
        end = len(nums)-1
        return DFS(start,end,nums)