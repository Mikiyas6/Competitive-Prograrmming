class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hashmap = defaultdict(list)
        for u, v in prerequisites:
            hashmap[u].append(v)
        
        output = []
        visited = set()
        path = set()

        def dfs(node):
            
            if node in path:
                return False
            if node in visited:
                return True
            
            neighbours = hashmap[node]
            path.add(node)
            for neighbour in neighbours:
                if not dfs(neighbour):
                    return False

            output.append(node)
            visited.add(node)
            path.remove(node)
            return True
        
        for node in range(numCourses):
            if node in visited and node not in output:
                output.append(node)
            else:
                if not dfs(node):
                    return []
        
        return output

