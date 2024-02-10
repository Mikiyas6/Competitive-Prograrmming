class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counts = [0] * 26  # Assuming only uppercase English letters
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1

        max_freq = max(task_counts)
        max_freq_count = task_counts.count(max_freq)

        # Calculate the minimum number of units of time required
        min_time = (max_freq - 1) * (n + 1) + max_freq_count

        # If the tasks are more than the minimum time, return the tasks length
        return max(len(tasks), min_time)
