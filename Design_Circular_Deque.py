class MyCircularDeque:

    def __init__(self, k: int):

        self.size = k
        self.queue = [None] * self.size
        self.front, self.rear = -1, -1

    def insertFront(self, value: int) -> bool:
        
        if self.isFull():

            return False
        
        if self.isEmpty():

            self.front = self.rear = 0
        
        else:

            self.front = (self.front - 1 + self.size) % self.size
        
        self.queue[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:

        if self.isFull():

            return False
        
        if self.isEmpty():

            self.front = self.rear = 0
        
        else:

            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = value

        return True

    def deleteFront(self) -> bool:
        
        if self.isEmpty():

            return False
        
        if self.front == self.rear:

            self.front = self.rear = -1
        
        else:
        
            self.front = (self.front + 1) % self.size
        
        return True

    def deleteLast(self) -> bool: 
        
        if self.isEmpty():

            return False
        
        if self.front == self.rear:

            self.front = self.rear = -1
        
        else:
        
            self.rear = (self.rear - 1 + self.size) % self.size

        return True

    def getFront(self) -> int:
        
        if self.isEmpty():

            return -1
        
        return self.queue[self.front]

    def getRear(self) -> int:
        
        if self.isEmpty():

            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool: 
        
        if self.front == -1 and self.rear == -1:
            return True

    def isFull(self) -> bool: 
        
        if (self.rear + 1) % self.size == self.front:
            return True


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
