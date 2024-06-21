class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        path = set()

        def dfs(node):

            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if not dfs(neighbor):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True