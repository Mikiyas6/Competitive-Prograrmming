class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.limit = k
        self.stream = deque()
        self.counter = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)

        if num == self.value:
            self.counter += 1

        if len(self.stream) > self.limit:
            removed = self.stream.popleft()
            if removed == self.value:
                self.counter -= 1

        return self.counter == self.limit

# # Your DataStream object will be instantiated and called as such:
# # obj = DataStream(value, k)
# # param_1 = obj.consec(num)

