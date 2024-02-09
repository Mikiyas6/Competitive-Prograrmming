class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on the second element

        dp = [1] * len(pairs)  # Initialize dp array with 1 (minimum chain length is 1)

        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:  # If the current pair can follow the previous pair
                    dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the chain

        return max(dp)
