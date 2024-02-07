class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # If nums[left] + nums[right] > nums[i], then all pairs in the range (left, right] will satisfy the condition
                    count += right - left
                    right -= 1
                else:
                    # If nums[left] + nums[right] <= nums[i], then we need to increase the left pointer to increase the sum
                    left += 1
        
        return count
