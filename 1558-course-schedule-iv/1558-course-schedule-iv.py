class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        if not prerequisites:
            return [False]*numCourses
        
        hashmap = defaultdict(list)
        for u, v in prerequisites:
            hashmap[v].append(u)
        
        visited = set()
        def bfs(start,end):

            queue = deque([start])
            while queue:
                node = queue.popleft()
                
                neighbours = hashmap[node]
                visited.add(node)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        if neighbour == end:
                            return True
                        queue.append(neighbour)
                        
            return False
            
        result = []
        for start, end in queries:
            result.append(bfs(end,start))
            visited = set()
        
        return result



            