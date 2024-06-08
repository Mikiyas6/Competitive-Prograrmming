class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combinations = []
        
        def dfs(i,comb,total):

            if total == target:
                combinations.append(comb[:])
                return
            
            if i == len(candidates) or total > target:
                return 
            
            comb.append(candidates[i])
            dfs(i,comb,total+candidates[i])

            comb.pop()
            dfs(i+1,comb,total)

            return 
        
        dfs(0,[],0)

        return combinations
