class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cumulative = 0
        prefix_sum = []
        for num in nums:
            cumulative += num
            prefix_sum.append(cumulative)
        for index in range(len(nums)):
            if prefix_sum[index] - nums[index] == prefix_sum[-1] - prefix_sum[index]:
                return index
        return -1
