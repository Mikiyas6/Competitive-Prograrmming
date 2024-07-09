class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n 

        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != -1:
                    return False  
                parent[leftChild[i]] = i
            
            if rightChild[i] != -1:
                if parent[rightChild[i]] != -1:
                    return False 
                parent[rightChild[i]] = i

        root_count = 0
        root = -1
        for i in range(n):
            if parent[i] == -1:  
                root_count += 1
                root = i
        
        if root_count != 1:
            return False  

        class UnionFind:
            def __init__(self, size):
                self.root = list(range(size))
                self.rank = [1] * size
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1
                else:
                    return False  
                return True

        uf = UnionFind(n)
        for i in range(n):
            if leftChild[i] != -1:
                if not uf.union(i, leftChild[i]):
                    return False
            if rightChild[i] != -1:
                if not uf.union(i, rightChild[i]):
                    return False
        
        return True