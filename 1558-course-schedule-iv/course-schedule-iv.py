class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        if not prerequisites:
            return [False] * len(queries)
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        ancestors = defaultdict(set)

        def dfs(node):

            if ancestors[node]:
                return ancestors[node]

            parents = graph[node]
            for parent in parents:
                ancestors[node].add(parent)
                ancestors[node].update(dfs(parent))
            
            return ancestors[node]

        for node in range(numCourses):
            ancestors[node] = dfs(node)

        result = []
        for u, v in queries:
            result.append(u in ancestors[v])
        return result