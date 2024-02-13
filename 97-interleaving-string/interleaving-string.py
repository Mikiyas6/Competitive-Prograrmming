class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize a 2D array dp
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Base case: when s1 and s2 are both empty, s3 is empty too, so it's an interleaving
        dp[0][0] = True

        # Fill the dp table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[len(s1)][len(s2)] 