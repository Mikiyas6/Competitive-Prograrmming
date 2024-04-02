class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        MOD = 12345

        n = len(grid)

        m = len(grid[0])

        prefix_product = [[1]*m for _ in range(n)]

        product_matrix = [[1]*m for _ in range(n)]

        suffix_product = [[1]*m for _ in range(n)]

        product = 1

        for row in range(n):

            for col in range(m):

                prefix_product[row][col] = product

                product *= grid[row][col]

                product %= MOD

        
        product = 1

        for row in range(n-1,-1,-1):

            for col in range(m-1,-1,-1):

                suffix_product[row][col] =  product

                product *= grid[row][col]

                product %= MOD
        

        for row in range(n):

            for col in range(m):

                product_matrix[row][col] = (prefix_product[row][col] * suffix_product[row][col]) % MOD

        return product_matrix
        




        