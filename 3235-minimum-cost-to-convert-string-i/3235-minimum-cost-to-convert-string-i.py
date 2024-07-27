class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        import sys
        INF = sys.maxsize
        
        # Step 1: Create the cost matrix
        cost_matrix = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            cost_matrix[i][i] = 0
        
        for o, c, z in zip(original, changed, cost):
            cost_matrix[ord(o) - ord('a')][ord(c) - ord('a')] = min(cost_matrix[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        # Step 2: Floyd-Warshall algorithm to compute all-pairs shortest path
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if cost_matrix[i][k] < INF and cost_matrix[k][j] < INF:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # Step 3: Calculate the minimum cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if cost_matrix[s_idx][t_idx] == INF:
                return -1
            total_cost += cost_matrix[s_idx][t_idx]
        
        return total_cost