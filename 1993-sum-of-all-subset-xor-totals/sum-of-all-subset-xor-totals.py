class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def fun(processed,unprocessed):

            if not unprocessed:

                total = 0
                for value in processed:
                    total ^= value
                
                return total

            return fun(processed+[unprocessed[0]],unprocessed[1:]) + fun(processed,unprocessed[1:])
        
        return fun([],nums)

        
        
     

