class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        # Sort the array
        nums.sort()
        
        # Find the median (middle element if length is odd, average of middle elements if length is even)
        median = nums[len(nums) // 2] if len(nums) % 2 != 0 else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
        
        # Calculate the sum of absolute differences between each element and the median
        moves = sum(abs(num - median) for num in nums)
        
        return moves
