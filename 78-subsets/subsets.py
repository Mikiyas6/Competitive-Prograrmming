class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def fun(processed,unprocessed):

            if not unprocessed:
                return [processed]
            
            return fun(processed + [unprocessed[0]], unprocessed[1:]) + fun(processed, unprocessed[1:])
        
        return fun([],nums)

            
            


