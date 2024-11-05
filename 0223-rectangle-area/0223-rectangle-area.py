class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_first = abs(ax1 - ax2) * abs(ay1 - ay2)
        area_second = abs(bx1 - bx2) * abs(by1 - by2)
        x_distance = (min(ax2, bx2) -max(ax1, bx1))
        y_distance = (min(ay2, by2) -max(ay1, by1))
        Area = 0
        if x_distance > 0 and y_distance > 0:
            Area = x_distance * y_distance
        return (area_first + area_second - Area)