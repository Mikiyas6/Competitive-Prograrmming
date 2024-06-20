class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [0]*len(graph)

        def bfs(i):

            if color[i]:
                return True
            
            queue = deque([i])
            color[i] = -1

            while queue:

                level = len(queue)
                node = queue.popleft()

                for _ in range(level):
                    neighbors = graph[node]
                    for neighbor in neighbors:
                        if color[neighbor] and color[neighbor] == color[node]:
                            return False

                        elif not color[neighbor]:
                            color[neighbor] = color[node] * -1
                            queue.append(neighbor)
            
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        
        return True

                        