class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        cumulative = 0
        prefix_sum = [0] * (len(nums)+2)

        for index,value in enumerate(nums):

            cumulative += value
            prefix_sum[index+1] = cumulative
        
        for r in range(1,len(prefix_sum)-1):

            if prefix_sum[r-1] == prefix_sum[len(prefix_sum)-2] - prefix_sum[r]:

                return r-1
        
        return -1
