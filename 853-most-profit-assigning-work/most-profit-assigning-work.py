class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        jobs = sorted(zip(difficulty, profit))  # Create a list of tuples and sort based on difficulty
        worker.sort()  # Sort the worker abilities
        total_profit = 0
        i = 0
        best = 0

        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])  # Find the best profit for current ability
                i += 1
            total_profit += best

        return total_profit