class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]  # Only one node in the tree

        graph = defaultdict(list)
        degrees = [0] * n

        # Build the graph and calculate the degrees of each node
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        leaves = deque([i for i in range(n) if degrees[i] == 1])

        # BFS to trim the tree
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()

            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = graph[leaf][0]

                # Remove the edge between leaf and neighbor
                graph[leaf].remove(neighbor)
                graph[neighbor].remove(leaf)
                degrees[neighbor] -= 1

                if degrees[neighbor] == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return list(leaves)
