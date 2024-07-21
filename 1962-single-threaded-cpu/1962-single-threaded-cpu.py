class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        indexed_tasks.sort()
        available_tasks = []
        
        result = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or available_tasks:
            while i < n and indexed_tasks[i][0] <= time:
                heapq.heappush(available_tasks, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            
            if available_tasks:
                processing_time, index = heapq.heappop(available_tasks)
                time += processing_time
                result.append(index)
            else:
                time = indexed_tasks[i][0]
        
        return result