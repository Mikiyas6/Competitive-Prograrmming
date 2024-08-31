class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        start = 0 
        max_length = 1  

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1 
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]

       