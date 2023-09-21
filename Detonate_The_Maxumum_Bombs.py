class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        bomb_adjacency = collections.defaultdict(list)
        n = len(bombs)
        
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if distance <= r1:
                    bomb_adjacency[i].append(j)
                if distance <= r2:
                    bomb_adjacency[j].append(i)
        
        def dfs(bomb_index, visited):
            if bomb_index in visited:
                return 0
            visited.add(bomb_index)
            for neighbor in bomb_adjacency[bomb_index]:
                dfs(neighbor, visited)
            return len(visited)
        
        max_detonation = 0
        for i in range(n):
            max_detonation = max(max_detonation, dfs(i, set()))
        
        return max_detonation
