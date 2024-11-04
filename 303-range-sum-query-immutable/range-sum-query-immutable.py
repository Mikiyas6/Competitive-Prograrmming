class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.result = [0]
        self.total = 0

        for value in self.nums:
            self.total += value
            self.result.append(self.total)

    def sumRange(self, left: int, right: int) -> int:
        return self.result[right+1] - self.result[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)