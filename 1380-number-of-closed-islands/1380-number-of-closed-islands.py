class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        dic={}
        vis=[]
        def fun(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            if [i,j] in vis:
                return True
            if grid[i][j]==1:
                return True
            vis.append([i,j])
            dic[i,j]=fun(i+1,j) and fun(i-1,j) and fun(i,j+1) and fun(i,j-1)
            return dic[i,j]
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in dic and grid[i][j]==0 and fun(i,j):
                    c+=1
                vis=[]
        return c