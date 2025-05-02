class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []        

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        
        if self.out_stack:
            return self.out_stack.pop()
        else:
            self.transfer()
            return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        else:
            self.transfer()
            return self.out_stack[-1]

    def empty(self) -> bool:

        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            return True
        else:
            return False
    
    def transfer(self) -> None:
        while self.in_stack:
            popped = self.in_stack.pop()
            self.out_stack.append(popped)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()