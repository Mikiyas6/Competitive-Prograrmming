class MyCircularQueue:

    def __init__(self, k: int):
        
        self.size = k
        self.queue = [0] * self.size
        self.left = self.right = -1

    def enQueue(self, value: int) -> bool:

        if self.isFull():

            return False

        if self.isEmpty():

            self.left = 0

        self.right = (self.right + 1) % self.size

        self.queue[self.right] = value

        return True

    def deQueue(self) -> bool:
        
        if self.isEmpty():

            return False
        
        if self.left == self.right and self.left != -1:

            self.left = self.right = -1
        
        else:

            self.left = (self.left + 1) % self.size
        
        return True

    def Front(self) -> int:
        
        if not self.isEmpty():

            return self.queue[self.left]
        
        return -1

    def Rear(self) -> int:
        
        if not self.isEmpty():

            return self.queue[self.right]
        
        return -1

    def isEmpty(self) -> bool:
        
        if self.left == self.right and self.left == -1:

            return True
        
        return False

    def isFull(self) -> bool:
        
        if (self.right + 1) % self.size == self.left:

            return True
        
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
