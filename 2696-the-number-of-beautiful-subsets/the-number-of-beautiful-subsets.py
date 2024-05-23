class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        nums.sort()  # Sort the array to handle elements in ascending order
        count = 0

        def backtrack(start, current):
            nonlocal count
            if current:
                count += 1

            for i in range(start, len(nums)):
                if any(abs(nums[i] - x) == k for x in current):
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return count
