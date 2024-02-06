class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Edge case: If the array has less than 3 elements, no need for processing
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # Pointer for the next position to place a unique element
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:  # Check if the current element is distinct
                nums[slow] = nums[fast]  # Place the distinct element at the slow pointer
                slow += 1  # Increment the slow pointer

        return slow


