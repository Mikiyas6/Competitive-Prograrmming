class MyQueue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:

        self.stack1.append(x)

    def pop(self) -> int:
        
        if not self.empty():

            for i in range(len(self.stack1)-1,0,-1):

                self.stack2.append(self.stack1.pop())
            
            value = self.stack1.pop()

            for i in range(len(self.stack2)-1,-1,-1):

                self.stack1.append(self.stack2[i])
            
            self.stack2 = []

            return value

    def peek(self) -> int:
        
        if not self.empty():
            return self.stack1[0]

    def empty(self) -> bool:
        
        if not self.stack1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
