class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        i = 0
        j = 0
        while j < n:
            while j < n and nums[j] == 0:
                j += 1
            if j < n:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
                j += 1
        return nums