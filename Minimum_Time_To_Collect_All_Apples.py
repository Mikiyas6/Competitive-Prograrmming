class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacency_list = [[] for _ in range(n + 1)]

        for edge in edges:
            node1, node2 = edge
            adjacency_list[node2].append(node1)
            adjacency_list[node1].append(node2)

        return self.calculate_time(adjacency_list, hasApple, 0, -1)

    def calculate_time(self, adjacency_list, hasApple, current_node, parent_node):
        time = 0
        for neighbor in adjacency_list[current_node]:
            if neighbor != parent_node:
                time += self.calculate_time(adjacency_list, hasApple, neighbor, current_node)

        if current_node == 0:
            return time

        if time == 0 and not hasApple[current_node]:
            return 0
        else:
            return time + 2
