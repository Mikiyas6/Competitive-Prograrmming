class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.prefix_sum = [0] * len(nums)
        self.cumulative = 0

        for index,value in enumerate(nums):

            self.cumulative += value
            self.prefix_sum[index] = self.cumulative
        
        self.prefix_sum = [0] + self.prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix_sum[right+1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)