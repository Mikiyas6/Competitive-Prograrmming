class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort()

        n = len(tasks)

        j = n - 1

        max_total = 0

        for time in processorTime:

            counter = 0

            total = 0

            while counter < 4:

                total = max(total,time + tasks[j])

                counter += 1

                j -= 1
            
            max_total = max(max_total,total)
        
        return max_total
        
