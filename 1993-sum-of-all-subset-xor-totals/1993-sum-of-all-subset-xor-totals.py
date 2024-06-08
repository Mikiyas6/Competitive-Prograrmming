class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def fun(i,total):

            if i == len(nums):
                return total
            
            return fun(i+1,total^nums[i]) + fun(i+1,total)
        
        return fun(0,0)
        
        # def fun(processed,unprocessed):

        #     if not unprocessed:

        #         total = 0
        #         for value in processed:
        #             total ^= value
                
        #         return total

        #     return fun(processed+[unprocessed[0]],unprocessed[1:]) + fun(processed,unprocessed[1:])
        
        # return fun([],nums)

        
        
     

