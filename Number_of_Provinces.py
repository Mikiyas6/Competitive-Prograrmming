class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    adjacency_list[i].append(j)
        visited_nodes = set()
        
        def depth_first_search(adjacency_list, visited, node):
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    depth_first_search(adjacency_list, visited, neighbor)
        
        num_provinces = 0
        for i in range(len(isConnected)):
            if i not in visited_nodes:
                num_provinces += 1
                depth_first_search(adjacency_list, visited_nodes, i)
                
        return num_provinces
