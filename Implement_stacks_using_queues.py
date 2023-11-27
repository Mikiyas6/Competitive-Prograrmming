class MyStack:

    def __init__(self):
        # Pop all the elements from queue1 to queue2 keeping the properties of queues
        # Add the element to queue1
        # Pop all the elements from queue2 back to queue1 keeping the properties of queues

        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        
        while self.queue1:

            self.queue2.append(self.queue1.popleft())
        
        self.queue1.append(x)

        while self.queue2:

            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        
        if not self.empty():

            return self.queue1.popleft()


    def top(self) -> int:
        
        if not self.empty():

            return self.queue1[0]

    def empty(self) -> bool:
        
        return True if not self.queue1 else False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
