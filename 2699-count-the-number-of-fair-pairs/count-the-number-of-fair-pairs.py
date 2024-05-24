class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        sortingData=[nums[-1]]
        n=len(nums)
        answer=0
        for i in range(n-2, -1, -1):
            l=bisect.bisect_left(sortingData, lower-nums[i])
            u=bisect.bisect_right(sortingData, upper-nums[i])            
            answer+=(u-l)
            bisect.insort_left(sortingData, nums[i])
        return answer