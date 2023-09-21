class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for src, dest in dislikes:
            adjacency_list[src - 1].append(dest - 1)
            adjacency_list[dest - 1].append(src - 1)
        
        
        node_colors = [0] * n
        
        
        def dfs(node, color):
            if node_colors[node] != 0:
                return node_colors[node] == color
            
            node_colors[node] = color
            for neighbor in adjacency_list[node]:
                if not dfs(neighbor, -color):
                    return False
        
            return True
        
        
        for i in range(n):
            if node_colors[i] == 0:
                if not dfs(i, 1):
                    return False
        
       
        return True
