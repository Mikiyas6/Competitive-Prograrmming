class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.lists = []
    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right+1])
        if len(self.lists) == 0:
            for i in range(len(self.nums)):
                if len(self.lists) == 0:
                    self.lists.append(self.nums[i])
                else:
                    self.lists.append(self.nums[i]+self.lists[-1])
        if left == 0:
            return self.lists[right]
        return self.lists[right] - self.lists[left-1]
        
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
