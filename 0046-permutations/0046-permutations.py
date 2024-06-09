class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def fun(nums):

            permutations = []

            if len(nums) == 1:
                return [nums[:]]

            for i in range(len(nums)):
                n = nums.pop(0)
                perms = fun(nums)

                for value in perms:
                    value.append(n)
                
                permutations.extend(perms)
                nums.append(n)
            
            return permutations
        
        return fun(nums)