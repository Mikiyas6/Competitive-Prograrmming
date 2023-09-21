class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)  

        for i in range(1, len(parent)): 
            graph[parent[i]].append(i)  

        max_path_length = 1  

        def dfs(node):
            nonlocal max_path_length  
           
            longest_path_length = second_longest_path_length = 0

            for child in graph[node]:  
                path_length = dfs(child) 

                if s[child] != s[node]: 
                    if path_length > longest_path_length:
                        second_longest_path_length = longest_path_length
                        longest_path_length = path_length
                    elif path_length > second_longest_path_length:
                        second_longest_path_length = path_length

            # Update the maximum path length considering the current node.
            max_path_length = max(max_path_length, 1 + longest_path_length + second_longest_path_length)
            return longest_path_length + 1  # Return the longest path length rooted at the current node.

        dfs(0)  # Start the depth-first search from the root node.
        return max_path_length  # Return the computed maximum path length.
