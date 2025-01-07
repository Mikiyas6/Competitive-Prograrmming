class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        g = defaultdict(list)
        for start, end, tip in rides:
            g[start].append((end, end - start + tip))
        profit = {i : 0 for i in range(1, n + 1)}
        prev_best = 0
        for u in range(1, n + 1):
            prev_best = max(prev_best, profit[u])
            profit[u] = prev_best
            for v, w in g[u]:
                profit[v] = max(profit[v], profit[u] + w)
        return prev_best   