class NumArray:

    def __init__(self, nums: List[int]):

        self.cumulative = 0
        self.prefix_sum = [0] * (len(nums) + 1)

        for index,value in enumerate(nums):

            self.cumulative += value

            self.prefix_sum[index+1] = self.cumulative


    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix_sum[right+1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
