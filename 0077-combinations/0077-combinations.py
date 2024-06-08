class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []
        
        def dfs(start,combo):

            if len(combo) == k:
                combinations.append(combo[:])
                return
            
            for i in range(start,n+1):
                combo.append(i)
                dfs(i+1,combo)
                combo.pop()

        dfs(1,[])
        return combinations          