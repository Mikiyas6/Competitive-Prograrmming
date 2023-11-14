class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        total = 0
        sub_arrays = 0
        prefix_sums = {0: 1}

        for r in range(len(nums)):
            total += nums[r]

            if total - goal in prefix_sums:
                sub_arrays += prefix_sums[total - goal]

            prefix_sums[total] = prefix_sums.get(total, 0) + 1 # Registering my prefix sum at each stage

        return sub_arrays
