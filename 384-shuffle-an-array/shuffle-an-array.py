class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            # Choose a random index j from i to n-1
            j = random.randrange(i, n)
            # Swap nums[i] and nums[j]
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()