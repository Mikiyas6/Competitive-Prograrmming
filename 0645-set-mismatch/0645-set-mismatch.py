class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        # Step 3: Find the missing number
        missing_number = expected_sum - actual_sum
        
        # Step 4: Find the duplicate number
        duplicate_number = sum(nums) - sum(set(nums))
        
        return [duplicate_number, duplicate_number + missing_number]