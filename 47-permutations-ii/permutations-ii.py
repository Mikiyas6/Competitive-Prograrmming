class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start):
            if start == len(nums):
                permutations.append(nums[:])  # Append a copy of the current permutation
                return
            used = set()  # Use a set to keep track of used elements at this position
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue  # Skip if the element is already used at this position
                used.add(nums[i])  # Mark the element as used
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recur for the next index
                nums[start], nums[i] = nums[i], nums[start]  # Undo the swap

        permutations = []
        backtrack(0)
        return permutations