class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.size = len(nums)
        def dfs(perm,length):
            if length == self.size:
                self.result.append(perm[:])
                return
            for value in nums:
                if value not in perm:
                    dfs(perm+[value],length+1)
        dfs([],0)
        return self.result
