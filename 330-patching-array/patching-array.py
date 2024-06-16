class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        x = 1
        i = 0
        
        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                x += x
                patches += 1
        
        return patches