from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.target = value
        self.limit = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:

        self.queue.append(num)

        if num == self.target:
            self.count += 1
        
        if len(self.queue) > self.limit:
            removed = self.queue.popleft()

            if removed == self.target:
                self.count -= 1
                
        return self.count == self.limit



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
