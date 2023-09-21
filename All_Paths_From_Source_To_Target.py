class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        all_paths = []  
        def dfs(path, node):
            if node == len(graph) - 1:
                
                all_paths.append(path + [node])
            else:
                
                for neighbor in graph[node]:
                    dfs(path + [node], neighbor)
        
    
        dfs([], 0)
        return all_paths
