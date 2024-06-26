class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        print(graph)
        
        ancestors = defaultdict(set)
        
        def dfs(node):

            if ancestors[node]:
                return ancestors[node]
            
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            
            return ancestors[node]
        
        for node in range(n):
            ancestors[node] = dfs(node)
        
        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))
        return result
