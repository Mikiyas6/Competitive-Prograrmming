class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lists1 = [0] * len(nums)
        lists2 = [0] * len(nums)
        accumulator = 0

        for i in range(len(nums)):

            accumulator += nums[i]
            lists1[i] = accumulator
        
        nums = nums[::-1]
        accumulator = 0

        for j in range(len(nums)):

            accumulator += nums[j]
            lists2[j] = accumulator
        
        lists2 = lists2[::-1]
        
        for k in range(len(nums)):
            
            if lists1[k] == lists2[k]:
                return k
        
        return -1
