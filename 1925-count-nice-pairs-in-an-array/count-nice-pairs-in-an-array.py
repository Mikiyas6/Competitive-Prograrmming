class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        mod = 10**9 + 7
        rev = lambda x: int(str(x)[::-1])

        count = 0
        freq = {}
        for i in range(len(nums)):
            diff = nums[i] - rev(nums[i])
            count += freq.get(diff, 0)
            freq[diff] = freq.get(diff, 0) + 1

        return count % mod