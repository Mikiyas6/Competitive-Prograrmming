class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        perimeter = sum(matchsticks)
        if perimeter %4 != 0:
            return False

        sideLength = perimeter // 4
        sides = [0]*4

        matchsticks.sort(reverse = True)

        def dfs(i):

            if i == len(matchsticks):
                return True
            
            for j in range(4):

                if sides[j] + matchsticks[i] <= sideLength:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        
        return dfs(0)
