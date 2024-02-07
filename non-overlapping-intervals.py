class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        # Sort intervals based on end times
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = intervals[0][0] - 1  # Initialize last end time
        
        for interval in intervals:
            if interval[0] < last_end:  # Check for overlap
                count += 1
            else:
                last_end = interval[1]  # Update last end time
        
        return count
