class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        
        for u, v in richer:
            graph[v].append(u)
        
        answer = [-1] * n
        
        def dfs(node):
            if answer[node] != -1:
                return answer[node]
            
            min_quiet_person = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[min_quiet_person]:
                    min_quiet_person = candidate
            
            answer[node] = min_quiet_person
            return min_quiet_person
        
        for i in range(n):
            dfs(i)
        
        return answer