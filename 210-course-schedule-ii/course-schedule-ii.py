class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = defaultdict(int)
        hashmap = defaultdict(list)
        queue = deque([])
        sources = []

        for u, v in prerequisites:
            indegree[u] += 1
            graph[u].append(v)
            hashmap[v].append(u)
        
        for i in range(numCourses):
            if i not in graph:
                queue.append(i)
        
        def bfs(queue):

            topo_sort = []
            while queue:
                level = len(queue)
                for _ in range(level):
                    node = queue.popleft()
                    topo_sort.append(node)
                    neighbors = hashmap[node]
                    for neighbor in neighbors:
                        if indegree[neighbor] > 0:
                            indegree[neighbor] -= 1
                            if indegree[neighbor] == 0:
                                queue.append(neighbor)
            return topo_sort
        
        ans = bfs(queue)

        if len(ans) != numCourses:
            return []
        return ans
                    



        
        # hashmap = defaultdict(list)
        # for u, v in prerequisites:
        #     hashmap[u].append(v)
        
        # output = []
        # visited = set()
        # path = set()

        # def dfs(node):
            
        #     if node in path:
        #         return False
        #     if node in visited:
        #         return True
            
        #     neighbours = hashmap[node]
        #     path.add(node)
        #     for neighbour in neighbours:
        #         if not dfs(neighbour):
        #             return False

        #     output.append(node)
        #     visited.add(node)
        #     path.remove(node)
        #     return True
        
        # for node in range(numCourses):
        #     if node in visited and node not in output:
        #         output.append(node)
        #     else:
        #         if not dfs(node):
        #             return []
        
        # return output

