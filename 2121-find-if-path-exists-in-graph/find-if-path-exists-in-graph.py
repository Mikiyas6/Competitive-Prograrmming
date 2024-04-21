class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Build the adjacency list representation of the graph
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Perform DFS from the source vertex
        visited = set()
        stack = [source]
        while stack:
            current = stack.pop()
            if current == destination:
                return True
            visited.add(current)
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
        return False