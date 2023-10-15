class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if k > len(nums):
            return -1
        
        max_sum = sum(nums[:k])

        max_average = max_sum / k
    
        i = 0
        j = k

        while j < len(nums):

            max_sum = max_sum - nums[i] + nums[j]

            max_average = max(max_average, max_sum / k)

            i += 1
            j += 1

        return max_average
