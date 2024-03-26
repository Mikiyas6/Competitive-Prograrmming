class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        left_prefix_sum = [0]*n

        right_prefix_sum = [0]*n

        cumulative = 0

        for index, value in enumerate(nums):

            left_prefix_sum[index] = cumulative

            cumulative += value
        
        cumulative = 0
        
        for index in range(n-1,-1,-1):

            right_prefix_sum[index] = cumulative

            cumulative += nums[index]
        
        for index in range(n):

            if left_prefix_sum[index] == right_prefix_sum[index]:

                return index
        
        return -1

        
        # n = len(nums)

        # prefix_sum = [0] * (n+2)

        # cumulative = 0

        # for index,value in enumerate(nums):

        #     cumulative += value

        #     prefix_sum[index+1] = cumulative
        
        # for index,value in enumerate(prefix_sum[1:n+1]):

        #     left = prefix_sum[index]

        #     right = prefix_sum[n] - value

        #     if left == right:

        #         return index
        
        # return -1
            