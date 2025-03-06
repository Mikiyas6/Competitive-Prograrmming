class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        set1 = set()
        hashmap = defaultdict(int)
        a = 0
        for i in range(n):
            for j in range(n):
                if hashmap[grid[i][j]]:
                    a = grid[i][j]
                hashmap[grid[i][j]] += 1
                set1.add(grid[i][j])
        set2 = set(range(1,(n**2)+1))
        return [a,list(set2-set1)[0]]
        