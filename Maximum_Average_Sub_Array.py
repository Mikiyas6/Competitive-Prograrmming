class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if k > len(nums):
            return -1
        
        max_sum = sum(nums[:k])
        max_average = max_sum / k
    
        i = 1

        window_element = nums[i:k+i]

        window_size = len(window_element)

        j = 0

        while window_size == k:

            max_sum = max_sum - nums[i-1] + nums[k+j]
            max_average = max(max_average, max_sum / k)

            i += 1
            j += 1

            window_size = len(nums[i:k+i])

        return max_average
