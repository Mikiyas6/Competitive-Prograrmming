class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        total_operations = 0
    
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                count = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                total_operations += count - 1
                nums[i] = nums[i] // count
        
        return total_operations