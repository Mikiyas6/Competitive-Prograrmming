class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        end_up = self.size - 1
        current = self.head
        for _ in range(end_up):
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        end_up = index-1
        current = self.head
        for _ in range(end_up):
            current = current.next
        next = current.next
        node = ListNode(val)
        current.next = node
        node.next = next
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        if index >= self.size:
            return
        end_up = index-1
        current = self.head
        for _ in range(end_up):
            current = current.next
        current.next = current.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)