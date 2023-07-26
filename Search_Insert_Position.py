class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if target < nums[start]:
            return 0
        elif target > nums[end]:
            return len(nums)
        else:
            while end >= start:
                middle = start + (end - start)//2
                if target == nums[middle]:
                    return middle
                elif target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
        return start
