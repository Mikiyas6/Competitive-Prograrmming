class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def dfs(i,comb,total):
            if total >= target:
                if total == target:
                    self.result.append(comb[:])
                return
            for j in range(i,len(candidates)):
                dfs(j,comb+[candidates[j]],total+candidates[j])
        dfs(0,[],0)
        return self.result

