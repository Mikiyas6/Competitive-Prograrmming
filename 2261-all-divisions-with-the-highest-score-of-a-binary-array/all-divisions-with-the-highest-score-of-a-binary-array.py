class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        n = len(nums) + 1

        nums_left = [0] * n
        nums_right = [0] * n

        for i in range(1,n):

            if nums[i-1] == 0:

                nums_left[i] = nums_left[i-1] + 1
            
            else:

                nums_left[i] = nums_left[i-1]
        
        for i in range(n-2,-1,-1):

            if nums[i] == 1:

                nums_right[i] = nums_right[i+1] + 1
            
            else:

                nums_right[i] = nums_right[i+1]
        
        result = defaultdict(list)

        max_sum = 0

        for i in range(n):

            sum = nums_right[i] + nums_left[i]

            if sum >= max_sum:

                result[sum].append(i)

                max_sum = sum

        return result[max_sum]
        
            


            


