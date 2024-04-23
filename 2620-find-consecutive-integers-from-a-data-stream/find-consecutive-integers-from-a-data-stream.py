class DataStream:

    def __init__(self, value: int, k: int):
        
        self.queue = deque()
        self.value = value
        self.k = k
        self.size = 0
        self.counter = 0

    def consec(self, num: int) -> bool:
        
        if num == self.value:
            self.counter += 1

        self.queue.append(num)
        self.size += 1

        if self.size > self.k:

            popped = self.queue.popleft()
            if popped == self.value:
                self.counter -= 1
        
        return True if self.counter == self.k else False





# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)