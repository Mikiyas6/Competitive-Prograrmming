class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]
        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            left_max[0] = dp[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c-1] - 1, dp[c])
            right_max[-1] = dp[-1]
            for c in range(n-2, -1, -1):
                right_max[c] = max(right_max[c+1] - 1, dp[c])
            for c in range(n):
                dp[c] = points[r][c] + max(left_max[c], right_max[c])
        return max(dp)