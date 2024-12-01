class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def backtrack(total,path):
            if total == target:
                if sorted(path) not in result:
                    result.append(sorted(path[:]))
                return
            for j in range(n):
                if total + candidates[j] <= target:
                    total += candidates[j]
                    path.append(candidates[j])
                    backtrack(total,path)
                    total -= candidates[j]
                    path.pop()
        backtrack(0,[])
        return result