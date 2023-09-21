class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def Create_Adjacency_List(edges):

            from collections import defaultdict

            Graph = defaultdict(list)

            for edge in edges:
                Graph[edge[0]].append(edge[1])
                Graph[edge[1]].append(edge[0])
            return Graph

        def dfs(node,visited):

            if node == destination:
                return True
            for neighbor in Graph[node]:
                if neighbor in visited:
                    continue
                elif neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor,visited)
                    if result:
                        return True
            return False

        Graph = Create_Adjacency_List(edges)

        visited = set()

        boolean = dfs(source,visited)

        return boolean
