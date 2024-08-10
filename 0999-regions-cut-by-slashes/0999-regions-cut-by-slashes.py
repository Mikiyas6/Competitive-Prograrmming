class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                c = grid[i][j]
                
                if c == ' ':
                    union(root, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)
                elif c == '/':
                    union(root, root + 3)
                    union(root + 1, root + 2)
                elif c == '\\':
                    union(root, root + 1)
                    union(root + 2, root + 3)
                if j + 1 < n:
                    union(root + 1, 4 * (i * n + (j + 1)) + 3)
                if i + 1 < n:
                    union(root + 2, 4 * ((i + 1) * n + j))
        return sum(1 for i in range(4 * n * n) if find(i) == i)