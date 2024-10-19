class UnionFind:

    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.sum = collections.defaultdict(int)

    def add_and_merge(self, i: int, num: int) -> int:
        self.sum[i] = num
        if i - 1 in self.sum: self.union(i - 1, i)
        if i + 1 in self.sum: self.union(i, i + 1)
        rooti = self.find(i)
        return self.sum[rooti]

    def find(self, x: int) -> int:
        if self.root[x] != x: self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return
        if self.rank[rootx] > self.rank[rooty]: 
            self.root[rooty] = rootx
            self.sum[rootx] += self.sum[rooty]
        elif self.rank[rootx] < self.rank[rooty]: 
            self.root[rootx] = rooty
            self.sum[rooty] += self.sum[rootx]
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
            self.sum[rootx] += self.sum[rooty]

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        res = [0 for _ in range(n)]
        max_sum_segment = 0
        for i in range(n - 1, -1, -1):
            res[i] = max_sum_segment
            q = removeQueries[i]
            max_sum_segment = max(max_sum_segment, uf.add_and_merge(q, nums[q]))
        return res