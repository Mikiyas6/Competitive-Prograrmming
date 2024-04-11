class MinStack:

    def __init__(self):
        
        self.stack = []
        # self.min_stack = []
        # self.ptr = 0

    def push(self, val: int) -> None:
        
        self.stack.append(val)

        # if not self.min_stack:
        #     self.min_stack.append(val)

        # else:   

        #     self.min_stack.append(0)
        #     key = val
        #     j = len(self.min_stack) - 2

        #     while key > self.min_stack[j] and j >= 0:

        #         self.min_stack[j+1] = self.min_stack[j]
        #         j -= 1
            
        #     self.min_stack[j+1] = key
        #     self.ptr += 1

    def pop(self) -> None:

        if self.stack:
        
            value = self.stack.pop()

            # if value == self.min_stack[self.ptr]:

            #     self.min_stack.pop()
            #     self.ptr -= 1
                
    def top(self) -> int:

        if self.stack:
        
            return self.stack[-1]

    def getMin(self) -> int:
        
        if self.stack:

            return min(self.stack)
            # return self.min_stack[self.ptr]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()