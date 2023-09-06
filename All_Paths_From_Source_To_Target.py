class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        all_paths = []  # A list to store all the paths from source to target
        def dfs(path, node):
            if node == len(graph) - 1:
                # If we've reached the target node, add the path to all_paths
                all_paths.append(path + [node])
            else:
                # Recursively explore all neighbors of the current node
                for neighbor in graph[node]:
                    dfs(path + [node], neighbor)
        
        # Start the depth-first search from the source node (which is 0 in this case)
        dfs([], 0)
        return all_paths
