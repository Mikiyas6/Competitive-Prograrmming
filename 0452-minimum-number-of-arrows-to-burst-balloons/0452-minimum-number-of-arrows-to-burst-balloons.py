class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0

        # Sort the balloons based on their ending points
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        # Iterate through each balloon
        for start, balloon_end in points:
            # If the balloon's starting point is greater than the ending point of the previous balloon,
            # we need to shoot an arrow
            if start > end:
                arrows += 1
                end = balloon_end  # Update the ending point of the arrow
        return arrows