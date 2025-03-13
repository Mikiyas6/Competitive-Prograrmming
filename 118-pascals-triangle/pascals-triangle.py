class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Matrix = [[1]+([0]*(numRows-1)) for _ in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,numRows):
                total = Matrix[i-1][j-1] + Matrix[i-1][j]
                if total == 0:
                    break
                Matrix[i][j] = total
        result = []
        for i in range(numRows):
            result.append(Matrix[i][:i+1])
        return result