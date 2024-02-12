class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # Count the frequency of each unique number
        num_counts = Counter(nums)
        
        # Get the maximum number in nums
        max_num = max(nums)
        
        # Initialize dp array to store the maximum points for each number
        dp = [0] * (max_num + 1)
        
        # Base case: if only one unique number, return its points
        if len(num_counts) == 1:
            return list(num_counts.values())[0] * list(num_counts.keys())[0]
        
        # Iterate through numbers and calculate maximum points
        for num in range(1, max_num + 1):
            dp[num] = max(dp[num - 1], dp[num - 2] + num * num_counts[num])
        
        # Return the maximum points earned
        return dp[max_num]