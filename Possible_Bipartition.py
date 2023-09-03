class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create an adjacency list graph to represent dislikes.
        adjacency_list = [[] for _ in range(n)]
        for src, dest in dislikes:
            adjacency_list[src - 1].append(dest - 1)
            adjacency_list[dest - 1].append(src - 1)
        
        # Use an array to track the colors of nodes (0 for uncolored, 1 for color A, -1 for color B).
        node_colors = [0] * n
        
        # Depth-first search function to check if the graph can be bipartitioned.
        def dfs(node, color):
            if node_colors[node] != 0:
                return node_colors[node] == color
            
            node_colors[node] = color
            for neighbor in adjacency_list[node]:
                if not dfs(neighbor, -color):
                    return False
        
            return True
        
        # Iterate through each node to check if the graph can be bipartitioned.
        for i in range(n):
            if node_colors[i] == 0:
                if not dfs(i, 1):
                    return False
        
        # If all nodes are successfully colored, the graph can be bipartitioned.
        return True
