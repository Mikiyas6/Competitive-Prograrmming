class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict

        Graph = defaultdict(list)

        for i in range(len(isConnected)):
            flag = False
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    flag = True
                    Graph[i].append(j)
            if not flag:
                Graph[i].append(None)

    
        def dfs(node):

            visited.add(node)

            for neighbor in Graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()    
        counter = 0

        for i in range(len(Graph)):
            if i not in visited:
                dfs(i)
                counter += 1
        return counter

