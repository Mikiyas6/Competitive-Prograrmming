class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      
        parent = [i for i in range((len(edges)+1))]
        rank = [1]*(len(edges)+1)

        def find(node):

            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])

            return parent[node]

        def union(node1,node2):

            parent1,parent2 = find(node1),find(node2)

            if parent1 == parent2:
                return False
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                parent[parent1] = parent2
                rank[parent2] += 1

            return True
        
        for node1,node2 in edges:
            if not union(node1,node2):
                return [node1,node2]
        