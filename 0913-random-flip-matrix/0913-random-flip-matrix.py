class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m*n
        self.used = set()
        self.r = random.Random()

    def flip(self) -> List[int]:
        r = self.r.randint(0, self.total-1)
        while r in self.used:
            r = self.r.randint(0, self.total-1)
        self.used.add(r)
        return [r//self.n, r%self.n]

    def reset(self) -> None:
        self.used = set()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()