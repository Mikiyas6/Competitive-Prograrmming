class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.size = len(candidates)
        def dfs(i,comb,total):
            if total == target:
                self.result.append(comb[:])
                return
            if i >= self.size or total > target:
                return
            dfs(i,comb+[candidates[i]],total+candidates[i])
            dfs(i+1,comb,total)
        dfs(0,[],0)
        return self.result

        # self.result = []
        # def dfs(i,comb,total):
        #     if total >= target:
        #         if total == target:
        #             self.result.append(comb[:])
        #         return
        #     for j in range(i,len(candidates)):
        #         dfs(j,comb+[candidates[j]],total+candidates[j])
        # dfs(0,[],0)
        # return self.result

