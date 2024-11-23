class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        first_side,second_side,third_side = nums[0],nums[1],nums[2]
        total = first_side + second_side
        if total <= third_side:
            maxTotal = 0
        else:
            maxTotal = total + third_side
        left = 0
        for right in range(3,n):
            total -= nums[left]
            total += nums[right-1]
            left += 1
            if total <= nums[right]:
                continue
            maxTotal = max(maxTotal,total+nums[right])
        return maxTotal
