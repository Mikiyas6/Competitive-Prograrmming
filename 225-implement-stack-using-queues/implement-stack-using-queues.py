class MyStack:

    def __init__(self):
        
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        
        self.queue1.append(x)

    def pop(self) -> int:
        
        if not self.queue2:

            while self.queue1:

                self.queue2.append(self.queue1.pop())
        
        else:

            while self.queue1:

                self.queue2.appendleft(self.queue1.popleft())
        
        return self.queue2.popleft()

    def top(self) -> int:
        
        if not self.queue2:

            while self.queue1:

                self.queue2.append(self.queue1.pop())
        
        else:

            while self.queue1:

                self.queue2.appendleft(self.queue1.popleft())

        
        return self.queue2[0]

    def empty(self) -> bool:
        
        if not self.queue1 and not self.queue2:

            return True
        
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()