class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes

        timePoints_minutes = [time_to_minutes(time) for time in timePoints]
        timePoints_minutes.sort()

        min_diff = float('inf')
        for i in range(len(timePoints_minutes) - 1):
            diff = timePoints_minutes[i + 1] - timePoints_minutes[i]
            min_diff = min(min_diff, diff)

        # Consider the circular nature of time
        diff_between_end_and_start = 24 * 60 - timePoints_minutes[-1] + timePoints_minutes[0]
        min_diff = min(min_diff, diff_between_end_and_start)

        return min_diff
