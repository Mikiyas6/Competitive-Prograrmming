class MyQueue:
    def __init__(self):
        # Stack to handle incoming elements
        self.in_stack = []
        # Stack to return elements from. It properly reverse the order for queue behavior
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        - If there are elements inside the out_stack, remove the element at the top of the stack and return it.
        - If there are no elements inside the out_stack, We will proceed to Transfer elements from in_stack to out_stack. And then, we will do the same thing as above, (i.e remove and return the value at the top of the out_stack) 

        Amortized Time Complexity: O(1)
        Worst-case Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.out_stack:
            return self.out_stack.pop()
        else:
            self._transfer()
            return self.out_stack.pop()

    def peek(self) -> int:
        """
        - If there are elements inside the out_stack, return the element at the top of the stack without removing it.
        - If there are no elements Inside the out_stack, We will proceed to Transfer elements from in_stack to out_stack. And then, we will return the value at the top of the out_stack (also without removing it)

        Amortized Time Complexity: O(1)
        Worst-case Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.out_stack:
            return self.out_stack[-1]
        else:
            self._transfer()
            return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns True if it's empty and False if it's not. 

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # The queue is empty if and only if both the stacks are empty. Else, If we have at least one element in either of the two stacks, it's not empty.
        if not self.in_stack and not self.out_stack:
            return True
        else:
            return False

    def _transfer(self):
        """
        Transfer all elements from in_stack to out_stack.
        This is done only when out_stack is empty and we need
        to perform pop or peek operation.

        Time Complexity: O(n) (only when transferring)
        Space Complexity: O(1)
        """
        while self.in_stack:
            popped_value = self.in_stack.pop()
            self.out_stack.append(popped_value)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()