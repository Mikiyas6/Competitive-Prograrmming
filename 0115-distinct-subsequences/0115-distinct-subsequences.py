class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def fun(s1, s2, ind1, ind2, dp):
            if ind2 < 0:
                return 1
            if ind1 < 0:
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            if s1[ind1] == s2[ind2]:
                leaveOne = fun(s1, s2, ind1 - 1, ind2 - 1, dp)
                stay = fun(s1, s2, ind1 - 1, ind2, dp)
                dp[ind1][ind2] = (leaveOne + stay)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2] = fun(s1, s2, ind1 - 1, ind2, dp)
                return dp[ind1][ind2]
    
        ls = len(s)
        lt = len(t)
        dp = [[-1 for i in range(lt)] for j in range(ls)]
        return fun(s,t,ls-1,lt-1,dp)
    
    