class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        hashmap = defaultdict(list)

        for u,v in edges:
            hashmap[u].append(v)
            hashmap[v].append(u)
        
        visited = set()
        def dfs(i):

            if i == n:
                return False
            
            if i == destination:
                return True
            
            neighbors = hashmap[i]
            visited.add(i)
            for neighbor in neighbors:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(source)