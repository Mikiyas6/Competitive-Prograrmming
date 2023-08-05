class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def Binary_Search(start,end,nums,target):
            if start > end:
                return -1
            middle = start + (end - start)//2
            if nums[middle] < target:
                start = middle + 1
                return Binary_Search(start,end,nums,target)
            elif nums[middle] > target:
                end = middle - 1
                return Binary_Search(start,end,nums,target)
            else:
                return middle
        start = 0
        end = len(nums) - 1
        return (Binary_Search(start,end,nums,target))
            
