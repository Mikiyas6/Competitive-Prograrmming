import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        
        ways = [0] * n
        ways[0] = 1
        dis = [float("inf")] * n
        dis[0] = 0
        
        
        heap = [(0, 0)]  
        
        while heap:
            time, node = heapq.heappop(heap)
            
            
            for neighbor, travel_time in adj[node]:
                new_time = time + travel_time
                
                
                if new_time == dis[neighbor]:
                    ways[neighbor] += ways[node]
                
                
                elif new_time < dis[neighbor]:
                    dis[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))
                    ways[neighbor] = ways[node]
        
        
        MOD = 10**9 + 7
        return ways[n-1] % MOD