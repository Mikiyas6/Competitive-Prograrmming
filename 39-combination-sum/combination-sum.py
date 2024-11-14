class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(total,path):

            if total == target:
                if sorted(path) not in result:
                    result.append(sorted(path[:]))
                return

            for i in range(len(candidates)):
                total += candidates[i]
                if total <= target:
                    path.append(candidates[i])
                    backtrack(total,path)
                    path.pop()
                total -= candidates[i]
            
        backtrack(0,[])
        return result