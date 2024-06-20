class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        adjacencyList = defaultdict(list)

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(i+1,len(bombs)):
                x2, y2, r2 = bombs[j]
                distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

                if r1 >= distance:
                    adjacencyList[i+1].append(j+1)
                if r2 >= distance:
                    adjacencyList[j+1].append(i+1)
        
        maxDet = 0
        visited = set()

        def dfs(i):

            if not adjacencyList[i]:
                visited.add(i)
                return
            
            visited.add(i)
            neighbors = adjacencyList[i]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
            
            return
        
        for i in range(1,len(bombs)+1):
            dfs(i)
            maxDet = max(maxDet,len(visited))
            visited = set()
        
        return maxDet
                