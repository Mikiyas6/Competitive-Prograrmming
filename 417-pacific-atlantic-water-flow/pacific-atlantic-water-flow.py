class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def inbound(row,col):
            return 0 <= row and row < m and 0 <= col and col < n

        def DFS(row,col,visited,ans):

            if len(ans) == 2:
                return True
        
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if not inbound(newRow,newCol):
                    if (newRow,newCol) in pacific_ocean:
                        ans.add('p')
                    if (newRow,newCol) in atlantic_ocean:
                        ans.add('a')
                else:
                    if (newRow,newCol) not in visited:
                        visited.add((newRow,newCol))
                        if heights[row][col] >= heights[newRow][newCol]:
                            if DFS(newRow,newCol,visited,ans):
                                return True
                        visited.remove((newRow,newCol))
            if len(ans) == 2:
                return True
            return False
        
        m = len(heights)
        n = len(heights[0])
        pacific_ocean = set()
        atlantic_ocean = set()
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        for row in range(m):
            pacific_ocean.add((row,-1))
            atlantic_ocean.add((row,n))
        for col in range(n):
            pacific_ocean.add((-1,col))
            atlantic_ocean.add((m,col))
        
        output = []
        for row in range(m):
            for col in range(n):
                if DFS(row,col,set(),set()):
                    output.append([row,col])
        return output
        

