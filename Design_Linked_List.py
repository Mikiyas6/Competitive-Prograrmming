class MyLinkedList:

    def __init__(self):
        self.list = []
        self.length = 0
    def get(self, index: int) -> int:
        if index >= self.length or self.length == 0:
            return -1 
        else:
            return self.list[index]
    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            self.list.append(val)
            self.length += 1
        else:
            self.list.insert(0,val)
            self.length += 1
    def addAtTail(self, val: int) -> None:
        self.list.append(val)
        self.length += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return -1
        else:
            self.list.insert(index,val)
            self.length += 1
    def deleteAtIndex(self, index: int) -> None:
        if self.length == 0 or index >= self.length:
            return - 1
        self.list.pop(index)
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
