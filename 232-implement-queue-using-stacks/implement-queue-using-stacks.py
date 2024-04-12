class MyQueue:

    def __init__(self):
        
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        
        for _ in range(self.size-1):

            self.stack2.append(self.stack1.pop())
        
        value = self.stack1.pop()
        self.size -= 1

        for _ in range(self.size):

            self.stack1.append(self.stack2.pop())
        
        return value
    def peek(self) -> int:
        
        for _ in range(self.size-1):

            self.stack2.append(self.stack1.pop())
        
        value = self.stack1[-1]

        for _ in range(self.size-1):

            self.stack1.append(self.stack2.pop())
        
        return value

    def empty(self) -> bool:
        
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()