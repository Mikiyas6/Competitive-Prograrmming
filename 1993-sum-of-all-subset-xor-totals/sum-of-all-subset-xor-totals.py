class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(index, current_xor):
            if index == len(nums):
                # Base case: all elements have been considered
                return current_xor
            
            # Recursive case: include or exclude the current element
            include = helper(index + 1, current_xor ^ nums[index])
            exclude = helper(index + 1, current_xor)
            
            # Return the sum of both cases
            return include + exclude
        
        # Start the recursion with the first element and initial XOR total as 0
        return helper(0, 0)