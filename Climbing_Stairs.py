class Solution:
    def climbStairs(self, n: int) -> int:

        n_steps = n
        
        if n_steps <= 2:
            return n_steps
    
        # Initialize an array to store the number of ways to reach each step
        ways_to_reach_step = [0] * (n_steps + 1)
        ways_to_reach_step[1] = 1
        ways_to_reach_step[2] = 2

        # Build the array using dynamic programming
        for current_step in range(3, n_steps + 1):
            ways_to_reach_step[current_step] = ways_to_reach_step[current_step - 1] + ways_to_reach_step[current_step - 2]

        return ways_to_reach_step[n_steps]
