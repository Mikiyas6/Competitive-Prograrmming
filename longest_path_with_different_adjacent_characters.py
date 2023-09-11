class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)  # Create a defaultdict to represent the graph.

        for i in range(1, len(parent)):  # Iterate through the 'parent' list to build the graph.
            graph[parent[i]].append(i)  # Add child nodes to the parent node in the graph.

        max_path_length = 1  # Initialize a variable to keep track of the maximum path length.

        def dfs(node):
            nonlocal max_path_length  
            # Initialize variables for the longest and second-longest path lengths.
            longest_path_length = second_longest_path_length = 0

            for child in graph[node]:  # Iterate through the child nodes of the current node.
                path_length = dfs(child)  # Recursively calculate the path length.

                if s[child] != s[node]:  # Check if the characters at the child and parent nodes are different.
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
