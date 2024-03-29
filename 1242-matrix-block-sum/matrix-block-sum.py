class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])

        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        def range_sum(row1, col1, row2, col2):
            return prefix_sum[row2 + 1][col2 + 1] - prefix_sum[row2 + 1][col1] - prefix_sum[row1][col2 + 1] + prefix_sum[row1][col1]

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row1, row2 = max(0, i - k), min(m - 1, i + k)
                col1, col2 = max(0, j - k), min(n - 1, j + k)
                result[i][j] = range_sum(row1, col1, row2, col2)

        return result