class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        total_servers = 0

        # Count the number of servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
                    total_servers += 1

        # Count the number of servers that communicate with any other server
        communication_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    communication_count += 1

        return communication_count