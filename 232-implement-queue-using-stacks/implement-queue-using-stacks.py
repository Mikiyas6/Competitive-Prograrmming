class MyQueue:
    def __init__(self):
        # Stack to handle incoming elements
        self.in_stack = []
        # Stack to reverse the order for queue behavior
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Time Complexity: O(1)
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        Amortized Time Complexity: O(1)
        """
        if self.out_stack:
            return self.out_stack.pop()
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        Amortized Time Complexity: O(1)
        """
        if self.out_stack:
            return self.out_stack[-1]
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        Time Complexity: O(1)
        """
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        """
        Transfer elements from in_stack to out_stack if out_stack is empty.
        This reverses the order to simulate queue behavior.
        """
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()