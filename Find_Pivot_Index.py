class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        cumulative = 0
        prefix_sum = [0] * (len(nums)+1)

        for index,value in enumerate(nums):

            cumulative += value
            prefix_sum[index+1] = cumulative
        
        last_element_index = len(prefix_sum) - 1
        
        for r in range(1,last_element_index+1):

            if prefix_sum[last_element_index] - prefix_sum[r] == prefix_sum[r-1]:

                return r-1
        
        return -1
