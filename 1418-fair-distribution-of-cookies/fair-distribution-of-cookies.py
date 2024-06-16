class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        positions = [0] * k
        min_unfairness = float('inf')

        def dfs(i):
            nonlocal min_unfairness
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(positions))
                return

            for j in range(k):
                positions[j] += cookies[i]
                if positions[j] < min_unfairness:
                    dfs(i + 1)
                positions[j] -= cookies[i]
                if positions[j] == 0:
                    break

        dfs(0)
        return min_unfairness