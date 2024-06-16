class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        positions = [0]*k
        min_value = float('inf')

        def dfs(i):

            nonlocal min_value
            if i == len(cookies):
                min_value = min(min_value,max(positions))
                return 

            if min_value <= max(positions):
                return

            for j in range(k):
                positions[j] += cookies[i]
                dfs(i+1)
                positions[j] -= cookies[i]
        
        dfs(0)
        return min_value