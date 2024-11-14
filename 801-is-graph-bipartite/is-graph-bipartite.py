class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def BFS():

            for i in range(len(graph)):
                queue = deque([i])
                hashmap = defaultdict(int)
                hashmap[i] = 0
                visited = set()
                while queue:
                    level = len(queue)
                    for _ in range(level):
                        node = queue.popleft()
                        neighbors = graph[node]
                        color = hashmap[node]
                        for neighbor in neighbors:
                            if neighbor in visited:
                                if hashmap[neighbor] == color:
                                    return False
                            else:
                                visited.add(neighbor)
                                hashmap[neighbor] = 1 if color == 0 else 0
                                queue.append(neighbor)
            return True

        return BFS()    
                    
