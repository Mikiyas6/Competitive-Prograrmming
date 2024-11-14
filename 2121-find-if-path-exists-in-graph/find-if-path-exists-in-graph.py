class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def backtrack(source,visited):

            if source == destination:
                return True

            neighbors = graph[source]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if backtrack(neighbor,visited):
                        return True
            
            return False
        
        visited = set()
        visited.add(source)
        return backtrack(source,visited)
