class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Create a DP table with (len(s) + 1) x (len(p) + 1) dimensions
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* etc., that can match empty string
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # '*' can match zero occurrences of the preceding element
                    dp[i][j] = dp[i][j-2]
                    # '*' can match one or more occurrences of the preceding element if it matches s[i-1]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    # Current characters match if they are equal or pattern has '.'
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]