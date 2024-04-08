class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:

            return -1
        
        current = self.head
        
        for i in range(index):

            current = current.next
        
        return current.val

    def addAtHead(self, val: int) -> None:

        Node = ListNode(val)
        Node.next = self.head
        self.head = Node
        self.size += 1
    
    def addAtTail(self, val: int) -> None:

        if not self.head:

            self.addAtHead(val)
            return
        
        end_up = self.size - 1
        
        Node = ListNode(val)
        current = self.head

        for i in range(end_up):

            current = current.next
        
        current.next = Node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:

            return
        
        if index == 0:

            self.addAtHead(val)
        
        elif index == self.size:

            self.addAtTail(val)
        
        else:

            end_up = index-1

            current = self.head

            for i in range(end_up):

                current = current.next
            
            temp = current.next
            Node = ListNode(val)
            current.next= Node
            Node.next = temp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:

            return

        if index == 0:

            self.deleteAtFirst()
        
        elif index == self.size-1:

            self.deleteAtEnd()
        
        else:

            end_up = index - 1

            current = self.head

            for i in range(end_up):

                current = current.next
            
            current.next = current.next.next
            self.size -= 1
        
    def deleteAtFirst(self) -> None:

        self.head = self.head.next
        self.size -= 1
    
    def deleteAtEnd(self) -> None:

        end_up = self.size - 2

        current = self.head

        for i in range(end_up):

            current = current.next
        
        current.next = None

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)