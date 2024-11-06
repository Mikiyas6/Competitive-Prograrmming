class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        count = sum(nums)
        currentcount = self.calculate(nums)
        maxcount = currentcount
        for i in range(1, n):
            currentcount = self.update(currentcount, count, n, nums[n - i])
            maxcount = max(maxcount, currentcount)
        return maxcount
    def calculate(self, nums: List[int]) -> int:
        """
        calculate currentcount(0)
        """
        return sum(i * num for i, num in enumerate(nums))
    def update(self, currentcount: int, count: int, n: int, lastelement: int) -> int:
        """
        update currentcount(i) based on currentcount(i - 1)
        """
        return currentcount + count - n * lastelement