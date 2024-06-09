class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        subsets = []

        def dfs(i,subset):

            if i >= len(nums):
                subsets.append(subset[:])
                return 
            
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,subset)
        
            return
        
        dfs(0,[])
        
        return subsets

        
