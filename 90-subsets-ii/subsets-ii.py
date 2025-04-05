class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.size = len(nums)
        def dfs(i,subset):
            if i >= self.size:
                self.result.append(subset[:])
                return
            dfs(i+1,subset+[nums[i]])
            while i+1 < self.size and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1,subset)
        dfs(0,[])
        return self.result
            
