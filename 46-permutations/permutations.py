class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start):
            if start == len(nums):
                permutations.append(nums[:])  # Append a copy of the current permutation
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recur for the next index
                nums[start], nums[i] = nums[i], nums[start]  # Undo the swap

        permutations = []
        backtrack(0)
        return permutations