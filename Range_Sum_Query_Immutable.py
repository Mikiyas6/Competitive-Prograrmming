class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.lists = [0] * len(self.nums)
        for i in range(len(self.nums)):
            if i == 0:
                self.lists[i] = self.nums[i]
            else:
                self.lists[i] = self.nums[i] + self.lists[i-1]
            
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.lists[right] - self.lists[left-1]
        return self.lists[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
