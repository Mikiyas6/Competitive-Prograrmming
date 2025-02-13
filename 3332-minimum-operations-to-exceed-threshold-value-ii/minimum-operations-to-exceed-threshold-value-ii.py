class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        counter = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums,min(x,y)* 2 + (max(x,y)))
            counter += 1
        return counter