class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
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

        i = 0
        j = i + 1

        result = []

        while j < len(nums):

            if nums[j] != nums[i]:

                result.append(nums[i])
            
            i += 1
            j += 1
        
        if nums[i] not in result:

            result.append(nums[i])

        return result