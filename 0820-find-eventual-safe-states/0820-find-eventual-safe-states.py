class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for index, value in enumerate(graph):
            hashmap[index] = value
        
        visited = set()
        path = set()

        def dfs(node):
            
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            neighbors = hashmap[node]
            for neighbor in neighbors:
                if not dfs(neighbor):
                    return False
            
            visited.add(node)
            path.remove(node)
            return True
        
        output = []

        for i in range(len(graph)):
            if dfs(i):
                output.append(i)

        return output
        