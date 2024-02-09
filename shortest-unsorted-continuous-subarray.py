class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 1:
            return 0

        # Find left boundary of the subarray
        left_boundary = 0
        while left_boundary < n - 1 and nums[left_boundary] <= nums[left_boundary + 1]:
            left_boundary += 1

        # If left boundary is already at the end, the array is already sorted
        if left_boundary == n - 1:
            return 0

        # Find right boundary of the subarray
        right_boundary = n - 1
        while right_boundary > 0 and nums[right_boundary] >= nums[right_boundary - 1]:
            right_boundary -= 1

        # Find minimum and maximum within the subarray
        min_val = min(nums[left_boundary:right_boundary + 1])
        max_val = max(nums[left_boundary:right_boundary + 1])

        # Expand the subarray to include any elements smaller than min_val or larger than max_val
        while left_boundary > 0 and nums[left_boundary - 1] > min_val:
            left_boundary -= 1
        while right_boundary < n - 1 and nums[right_boundary + 1] < max_val:
            right_boundary += 1

        return right_boundary - left_boundary + 1
