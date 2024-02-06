class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, path):
            result.append(path[:])  # Append the current subset to the result
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include the current element in the subset
                backtrack(i + 1, path)  # Recur with the next index and updated subset
                path.pop()
        
        result = []
        backtrack(0, [])  # Start backtracking from index 0 with an empty subset
        return result
