from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.timeline = SortedDict()

    def book(self, start: int, end: int) -> int:
        if start in self.timeline:
            self.timeline[start] += 1
        else:
            self.timeline[start] = 1
        
        if end in self.timeline:
            self.timeline[end] -= 1
        else:
            self.timeline[end] = -1
        
        active_events = 0
        max_k_booking = 0

        for count in self.timeline.values():
            active_events += count
            if active_events > max_k_booking:
                max_k_booking = active_events

        return max_k_booking
        
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)