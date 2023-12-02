class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        
        self.stack_push.append(x)

    def pop(self) -> int:

        if not self.stack_pop:

            while self.stack_push:

                self.stack_pop.append(self.stack_push.pop())
        
        return self.stack_pop.pop()

    def peek(self) -> int:
        
        if not self.stack_pop:

            while self.stack_push:

                self.stack_pop.append(self.stack_push.pop())
        
        return self.stack_pop[-1]

    def empty(self) -> bool:
        
        if not self.stack_push and not self.stack_pop:

            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
