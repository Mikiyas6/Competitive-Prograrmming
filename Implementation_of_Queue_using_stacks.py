class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # if len(self.stack2) == 0:
        #     self.stack1.append(x)
        # else:
        #     while len(self.stack2) > 0:
        #         last = self.stack2[-1]
        #         self.stack2.pop()
        #         self.stack1.append(last)
        #     self.stack1.append(x)
        self.stack1.append(x)
    def pop(self):
        """
        :rtype: int
        """
        # if len(self.stack1) == 0 and len(self.stack2) == 0:
        #     return None
        # elif len(self.stack1) > 0:
        #     while len(self.stack1) > 0:
        #         self.stack2.append(self.stack1.pop())
        # return self.stack2.pop()
        if (len(self.stack1) == 0 and len(self.stack2) == 0):
            return None
        elif (len(self.stack2) != 0):
            return self.stack2.pop()
        else:
            if (len(self.stack1) == 1):
                return self.stack1.pop()
            for i in range(len(self.stack1) - 1):
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()

    def peek(self):
        """
        :rtype: int
        """
        # if len(self.stack1) == 0 and len(self.stack2) == 0:
        #     return None
        # elif len(self.stack1) > 0:
        #     while len(self.stack1) > 0:
        #         self.stack2.append(self.stack1.pop())
        # return self.stack2[-1]
        if (len(self.stack1) == 0 and len(self.stack2) == 0):
            return None
        elif (len(self.stack2) != 0):
            return self.stack2[-1]
        elif (len(self.stack2) == 0 and len(self.stack1) != 0):
            if (len(self.stack1) == 1):
                return self.stack1[0]
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
            # for i in range(len(self.stack2)):
            #     self.stack1.append(self.stack2.pop())
            # return value

    def empty(self):
        """
        :rtype: bool
        """
        if(len(self.stack1) == 0 and len(self.stack2) == 0 ):
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
