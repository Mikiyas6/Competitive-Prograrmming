class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        def dfs(i,combo,length):
            if length == k:
                self.result.append(combo[:])
                return
            for j in range(i,n+1):
                dfs(j+1,combo+[j],length+1)
        dfs(1,[],0)
        return self.result
