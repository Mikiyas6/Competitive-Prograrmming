class RecentCounter:

    def __init__(self):
        
        self.queue = deque()

    def ping(self, t: int) -> int:
        
        left_edge = t - 3000

        self.queue.append(t)

        while self.queue and self.queue[0] < left_edge:

            self.queue.popleft()
        
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)