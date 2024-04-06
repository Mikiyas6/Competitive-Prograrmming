class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def fun(processed,unprocessed):

            if not unprocessed:

                return [processed]
            
            first_char = unprocessed[0]

            combinations = []

            for i in range(len(processed)+1):

                combinations.extend(fun(processed[:i]+[first_char]+processed[i:],unprocessed[1:]))
            
            return combinations
        
        nums = fun([],nums)

        nums.sort()

        return nums
        
        

