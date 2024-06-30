class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        def add_edge(f: str, t: str, value: float):
            if f not in graph:
                graph[f] = {}
            graph[f][t] = value
        
        for (dividend, divisor), value in zip(equations, values):
            add_edge(dividend, divisor, value)
            add_edge(divisor, dividend, 1 / value)
        
        def dfs(start: str, end: str, visited: Set[str]) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * value
            return -1.0
        
        results = []
        for dividend, divisor in queries:
            if dividend == divisor and dividend in graph:
                results.append(1.0)
            else:
                results.append(dfs(dividend, divisor, set()))
        
        return results