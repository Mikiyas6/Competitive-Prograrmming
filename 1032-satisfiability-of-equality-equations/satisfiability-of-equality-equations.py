class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind()
        for eq in equations:
            if eq[1] == "=":
                uf.union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == "!" and uf.find(eq[0]) == uf.find(eq[3]):
                return False

        return True

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y