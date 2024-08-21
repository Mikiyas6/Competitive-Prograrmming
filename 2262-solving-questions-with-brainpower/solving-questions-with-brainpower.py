class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        ######### Top-Down
        # n = len(questions)
        # memo = defaultdict(int)

        # def fun(i,total):

        #     if i >= n:
        #         return total
            
        #     if (i,total) not in memo:
        #         memo[(i,total)] = max(fun(i+1,total),fun(i+questions[i][1]+1,total+questions[i][0]))
            
        #     return memo[(i,total)]
        
        # return fun(0,0)

        # Bottom-up
        n = len(questions)
        dp = [0]*(n)

        dp[-1] = questions[-1][0]

        for i in range(n-2,-1,-1):
            index = i+questions[i][1]+1
            value = 0
            if index < n:
                value = dp[index]
            dp[i] = max(value+questions[i][0],dp[i+1])
        
        print(dp)
        return max(dp)

        
        # n = len(questions)
        # dp = [0]*(n)

        # for i in range(n):
        #     points, brainPower = questions[i]
        #     total = 0
        #     j = i+brainPower+1
        #     while j < n:
        #         total += questions[j][0]
        #         j += questions[j][1] + 1
        #     dp[i] = total+points
        
        # return max(dp)