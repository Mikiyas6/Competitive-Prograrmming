class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Step 1: Create a list of projects with (capital, profit) and sort by capital
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        
        # Step 2: Initialize two heaps
        min_cap_heap = []  # Min-heap for project capital requirements
        max_prof_heap = []  # Max-heap for available project profits
        
        # Step 3: Iterate up to k times to select projects
        index = 0
        for _ in range(k):
            # Move projects from min-heap to max-heap if the required capital is <= current capital
            while index < len(projects) and projects[index][0] <= w:
                heapq.heappush(max_prof_heap, -projects[index][1])
                index += 1
            
            # If there are no available projects, break the loop
            if not max_prof_heap:
                break
            
            # Select the project with the maximum profit
            w += -heapq.heappop(max_prof_heap)
        
        return w