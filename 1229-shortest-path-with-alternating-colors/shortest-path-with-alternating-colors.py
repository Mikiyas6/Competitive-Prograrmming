class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for u, v in redEdges:
            red_adj[u].append(v)
        
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        
        answer = [-1] * n
        answer[0] = 0
        
        
        queue = deque([(0, 0, 'red'), (0, 0, 'blue')])
        visited = set((0, 'red')) | set((0, 'blue'))
        
        while queue:
            node, dist, last_color = queue.popleft()
            
            if last_color == 'red':
                neighbors = blue_adj[node]
                next_color = 'blue'
            else:
                neighbors = red_adj[node]
                next_color = 'red'
            
            for neighbor in neighbors:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, dist + 1, next_color))
                    if answer[neighbor] == -1:
                        answer[neighbor] = dist + 1
        
        return answer