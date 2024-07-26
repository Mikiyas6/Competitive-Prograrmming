class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counts = [0] * 26  
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1

        max_freq = max(task_counts)
        max_freq_count = task_counts.count(max_freq)
        min_time = (max_freq - 1) * (n + 1) + max_freq_count
        return max(len(tasks), min_time)