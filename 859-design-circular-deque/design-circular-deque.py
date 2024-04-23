# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        if self.isEmpty():
            Node = ListNode(value)
            self.head = Node
            self.tail = Node
        else:
            Node = ListNode(value)
            Node.next = self.head
            self.head = Node
        
        self.size += 1
            
        return True

    def insertLast(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        if self.isEmpty():
            Node = ListNode(value)
            self.head = Node
            self.tail = Node
        else:
            Node = ListNode(value)
            self.tail.next = Node
            self.tail = Node
        
        self.size += 1
            
        return True

    def deleteFront(self) -> bool:
        
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        
        if self.size == 1:

            self.tail = None
        
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.head = self.head.next
            self.tail = None
        
        else:
        
            current = self.head
            while current.next.next:

                current = current.next
            
            current.next = None
            self.tail = current

        self.size -= 1

        return True

    def getFront(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.head.val

    def getRear(self) -> int:
        
        if self.isEmpty():
            return -1
        
        return self.tail.val

    def isEmpty(self) -> bool:

        return True if self.size == 0 else False
        
    def isFull(self) -> bool:

        return True if self.size == self.capacity else False
        

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