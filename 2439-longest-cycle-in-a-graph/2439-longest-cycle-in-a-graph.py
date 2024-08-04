class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node, visited, stack, distance):
            nonlocal max_cycle_length
            visited[node] = True
            stack[node] = True
            current_distance = distance[node]

            neighbor = edges[node]
            if neighbor != -1:
                if not visited[neighbor]:
                    distance[neighbor] = current_distance + 1
                    dfs(neighbor, visited, stack, distance)
                elif stack[neighbor]: 
                    cycle_length = current_distance - distance[neighbor] + 1
                    max_cycle_length = max(max_cycle_length, cycle_length)
            
            stack[node] = False
        
        n = len(edges)
        visited = [False] * n
        stack = [False] * n
        max_cycle_length = -1
        
        for i in range(n):
            if not visited[i]:
                distance = {i: 0}
                dfs(i, visited, stack, distance)
        
        return max_cycle_length