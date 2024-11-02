class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        def findDistance(row,col):
            return abs(rCenter-row) + abs(cCenter-col)
        
        result = []
        for row in range(rows):
            for col in range(cols):
                distance = findDistance(row,col)
                result.append((distance,[row,col]))
        
        result.sort()
        output = []
        for distance,grid in result:
            row,col = grid
            output.append([row,col])
        return output