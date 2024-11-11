class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(range(n))
        for u, v in edges: dsu.union(u, v)
        counts = Counter(map(dsu.find, range(n))).values()
        return sum(map(mul, accumulate(counts, add, initial=0), counts))


T = Hashable
class DSU:
    def __init__(self, xs: Iterable[T] = ()) -> None:
        self.parents: Mapping[T, T] = {x: x for x in xs}
        self.sizes: Mapping[T, int] = {x: 1 for x in xs}

    def find(self, u: T) -> T:
        self.parents[u] = u if self.parents[u] == u else self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u: T, v: T) -> None:
        ur, vr = self.find(u), self.find(v)
        if ur == vr: return
        low, high = (ur, vr) if self.sizes[ur] < self.sizes[vr] else (vr, ur)
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
    
    def is_connected(self, u: T, v: T) -> bool:
        return self.find(u) == self.find(v)
