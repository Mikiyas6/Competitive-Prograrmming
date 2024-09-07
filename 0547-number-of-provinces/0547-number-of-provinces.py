class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n, m = len(isConnected), len(isConnected[0])
        parent = [i for i in range(n)]
        rank = [1]*(n)

        def find(node):
            if node == parent[node]:
                return node
            
            parent[node] = find(parent[node])

            return parent[node]

        def union(node1,node2):

            parent1, parent2 = find(node1), find(node2)

            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                parent[parent1] = parent2
                rank[parent2] += 1
        
        for i in range(n):
            for j in range(i + 1, m):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        province_count = len(set(find(i) for i in range(n)))
        
        return province_count