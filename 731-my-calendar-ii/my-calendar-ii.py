class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        # Check if the new event would cause a triple booking
        for o_start, o_end in self.overlaps:
            if start < o_end and end > o_start:  # overlap with an overlap means a triple booking
                return False
        
        # Add to the overlaps list if it overlaps with existing bookings
        for b_start, b_end in self.bookings:
            if start < b_end and end > b_start:  # find intersection of new booking and existing booking
                overlap_start = max(start, b_start)
                overlap_end = min(end, b_end)
                self.overlaps.append((overlap_start, overlap_end))
        
        # Add the new booking to the bookings list
        self.bookings.append((start, end))
        return True
        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)