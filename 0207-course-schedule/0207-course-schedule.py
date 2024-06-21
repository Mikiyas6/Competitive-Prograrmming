class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        # Create two sets for visited and currently in path nodes
        visited = set()
        path = set()

        # Helper function for DFS
        def dfs(node):
            if node in path:  # cycle detected
                return False
            if node in visited:  # already processed node
                return True
            
            # Mark the current node in the path
            path.add(node)
            # Visit all the neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # Remove from current path and add to visited
            path.remove(node)
            visited.add(node)
            return True
        
        # Check all nodes
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True