class MedianFinder:

    def __init__(self):
        self.small_half = []  # Max heap
        self.large_half = []  # Min heap

    def addNum(self, num: int) -> None:
        if not self.small_half or num <= -self.small_half[0]:
            heappush(self.small_half, -num)
        else:
            heappush(self.large_half, num)
            
        if len(self.small_half) > len(self.large_half) + 1:
            heappush(self.large_half, -heappop(self.small_half))
        elif len(self.large_half) > len(self.small_half):
            heappush(self.small_half, -heappop(self.large_half))

    def findMedian(self) -> float:
        if len(self.small_half) == len(self.large_half):
            return (-self.small_half[0] + self.large_half[0]) / 2
        else:
            return -self.small_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()