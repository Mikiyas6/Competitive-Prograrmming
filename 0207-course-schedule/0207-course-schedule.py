class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        path = set()

        def dfs(node):
            
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if not dfs(neighbor):
                    return False
            
            visited.add(node)
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
        
        # graph = defaultdict(list)
        # for u, v in prerequisites:
        #     graph[u].append(v)
        
        # visited = set()
        # path = set() 

        # def dfs(node):

        #     if node in path:
        #         return False
        #     if node in visited:
        #         return True
            
        #     path.add(node)
        #     neighbors = graph[node]
        #     for neighbor in neighbors:
        #         if not dfs(neighbor):
        #             return False
            
        #     visited.add(node)
        #     path.remove(node)
        #     return True
        
        # for i in range(numCourses): #The loop is for if there are disconnected graphs
        #     if not dfs(i):
        #         return False
        
        # return True