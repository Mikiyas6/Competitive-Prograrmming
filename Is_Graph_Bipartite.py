class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        from collections import defaultdict

        visited = set()
        coloring = [0] * len(graph)

        def dfs(node):
            if node not in visited:
                visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    coloring[neighbour] = 1 - coloring[node]
                    if not dfs(neighbour):
                        return False

                if neighbour in visited and coloring[node] == coloring[neighbour]:
                    return False
            return True

        for i in range(len(graph)):
            if not dfs(i):
                return False
        return True
