class MyCircularDeque:

    def __init__(self, k: int):

        self.size = k
        self.Deque = [None] * self.size
        self.left = self.right = -1

    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        if self.left == self.right and self.left == -1:

            self.left = self.right = 0
        
        else:
        
            self.left = (self.left - 1 + self.size) % self.size

        self.Deque[self.left] = value

        return True

    def insertLast(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        if self.left == self.right and self.left == -1:

            self.left = self.right = 0
        
        else:
        
            self.right = (self.right + 1) % self.size

        self.Deque[self.right] = value

        return True

    def deleteFront(self) -> bool:
        
        if self.isEmpty():

            return False
        
        if self.left == self.right and self.left != -1:

            self.left = self.right = -1
        
        else:

            self.left = (self.left + 1) % self.size
        
        return True

    def deleteLast(self) -> bool:
        
        if self.isEmpty():

            return False
        
        if self.left == self.right and self.left != -1:

            self.left = self.right = -1
        
        else:

            self.right = (self.right - 1 + self.size) % self.size
        
        return True

    def getFront(self) -> int:
        
        if self.isEmpty():

            return -1
        
        return self.Deque[self.left]

    def getRear(self) -> int:
        
        if self.isEmpty():

            return -1
        
        return self.Deque[self.right]

    def isEmpty(self) -> bool:
        
        if self.left == self.right and self.left == -1:

            return True
        
        return False

    def isFull(self) -> bool:
        
        if (self.right + 1) % self.size == self.left:

            return True
        
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
