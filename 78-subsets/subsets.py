class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # self.result = []
        # def dfs(i,subset):
        #     if i == len(nums):
        #         self.result.append(subset[:])
        #         return
        #     dfs(i+1,subset+[nums[i]])
        #     dfs(i+1,subset)
        # dfs(0,[])
        # return self.result

        def dfs(i,subset):
            if i == len(nums):
                return [subset]
            left = dfs(i+1,subset+[nums[i]])
            right = dfs(i+1,subset)
            return left + right
        return dfs(0,[])