class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []

        def store(permutation):

            permutations.append(permutation[:])

        def fun(processed,unprocessed):

            if not unprocessed:
                store(processed)
                return
            
            preProcessed = processed
            for i in range(len(processed)+1):

                processed = processed[:i] + [unprocessed[0]] + processed[i:]
                fun(processed,unprocessed[1:])
                processed.pop(i)
            
            return
        
        fun([],nums)
        
        return permutations