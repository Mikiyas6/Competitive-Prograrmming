class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Fill the initial distances based on edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 3: Apply Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Count reachable cities for each city
        reachable_cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_cities[i] += 1
        
        # Step 5: Find the city with the smallest number of reachable cities
        min_reachable = float('inf')
        result_city = -1
        for i in range(n):
            if reachable_cities[i] < min_reachable or (reachable_cities[i] == min_reachable and i > result_city):
                min_reachable = reachable_cities[i]
                result_city = i
        
        return result_city