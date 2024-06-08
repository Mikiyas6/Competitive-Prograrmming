class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def fun(i,subset):

            if i == len(nums):

                return [subset]
            
            return fun(i+1,subset+[nums[i]]) + fun(i+1,subset)
        
        return fun(0,[])
            
            


