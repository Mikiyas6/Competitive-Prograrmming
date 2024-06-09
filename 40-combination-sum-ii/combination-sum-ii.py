class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combinations = []
        candidates.sort()

        def fun(i,combo,total):

            if total == target:
                combinations.append(combo[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            total += candidates[i]
            fun(i+1,combo,total)

            combo.pop()
            total -= candidates[i]

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            fun(i+1,combo,total)
        
        fun(0,[],0)

        return combinations


            
