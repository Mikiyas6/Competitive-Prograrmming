class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[len(nums)-1]
        for i in range(1,k):
                ans = ans+nums[len(nums)-1]+i
        return ans 