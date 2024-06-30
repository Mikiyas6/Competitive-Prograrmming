class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            
            def find(self, u):
                if self.parent[u] != u:
                    self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
            
            def union(self, u, v):
                root_u = self.find(u)
                root_v = self.find(v)
                
                if root_u != root_v:
                    if self.rank[root_u] > self.rank[root_v]:
                        self.parent[root_v] = root_u
                    elif self.rank[root_u] < self.rank[root_v]:
                        self.parent[root_u] = root_v
                    else:
                        self.parent[root_v] = root_u
                        self.rank[root_u] += 1
                    return True
                return False

        # Initialize Union-Find structures for Alice and Bob
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        edges_used = 0
        
        # Process type 3 edges first (usable by both Alice and Bob)
        for type, u, v in edges:
            if type == 3:
                if uf_alice.union(u, v):
                    uf_bob.union(u, v)
                    edges_used += 1

        # Process type 1 edges (usable by Alice only)
        for type, u, v in edges:
            if type == 1:
                if uf_alice.union(u, v):
                    edges_used += 1
        
        # Process type 2 edges (usable by Bob only)
        for type, u, v in edges:
            if type == 2:
                if uf_bob.union(u, v):
                    edges_used += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if len(set(uf_alice.find(i) for i in range(1, n + 1))) > 1 or len(set(uf_bob.find(i) for i in range(1, n + 1))) > 1:
            return -1
        
        # The maximum number of edges we can remove is the total number of edges minus the number of edges used
        return len(edges) - edges_used