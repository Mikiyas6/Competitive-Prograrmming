class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        n = len(nums)
        
        for i in range(n):

            for j in range(i+indexDifference,n):

                value_diff = abs(nums[i] - nums[j])
                
                if value_diff >= valueDifference:

                    return [i,j]
        
        return [-1,-1]