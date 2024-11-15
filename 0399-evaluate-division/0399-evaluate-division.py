class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        # Building Adjacency List
        for i in range(n):
            A,B = equations[i]
            graph[A].append([B,values[i]])
            graph[B].append([A,1/values[i]])

        def dfs(graph, start, end, path, visited):
            if start == end:  
                return path

            for neighbor in graph[start]:
                node, weight = neighbor
                if node not in visited:
                    visited.add(node)
                    path *= weight
                    result = dfs(graph, node, end, path, visited)
                    if result != -1:  
                        return result
                    path /= weight
            return -1  

        output = []
        for query in queries:
            node1,node2 = query
            if node1 not in graph or node2 not in graph:
                output.append(-1)
            elif node1 == node2:
                output.append(1)
            else:
                visited = set()
                visited.add(node1)
                result = dfs(graph,node1,node2,1,visited)
                output.append(result)
        
        return output