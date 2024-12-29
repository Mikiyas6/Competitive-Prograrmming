class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = int(1e9 + 7)
        n = len(words[0])
        m = len(target)
        freq = [collections.defaultdict(int) for _ in range(n)]
        for word in words:
            for i in range(n):
                freq[i][word[i]] += 1
        memo = [[-1] * (m + 1) for _ in range(n + 1)]

        def traverse(level, index):
            if index == m:
                return 1
            if level == n:
                return 0
            if memo[level][index] != -1:
                return memo[level][index]
            ways = traverse(level + 1, index)
            if target[index] in freq[level]:
                count = freq[level][target[index]]
                ways = (ways + count * traverse(level + 1, index + 1)) % MOD
            memo[level][index] = ways
            return ways

        return traverse(0, 0)