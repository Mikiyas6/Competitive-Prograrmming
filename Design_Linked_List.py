class MyLinkedList:
    class Node:
        def __init__(self):
            self.val = None
            self.next = None
        def set_item(self,val):
            self.val = val
        def get_item(self):
            return self.val
        def set_next(self,next):
            self.next = next
        def get_next(self):
            return self.next

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            current = self.head
            counter = 0
            while counter < index:
                counter += 1
                current = current.next
            if current == None:
                return -1
            return current.get_item()

    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            new_node = self.Node()
            new_node.set_item(val)
            new_node.set_next(None)
            self.head = new_node
        else:
            new_head = self.Node()
            new_head.set_item(val)
            new_head.next = self.head
            self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        current = self.head
        new_node = self.Node()
        new_node.set_item(val)
        new_node.set_next(None)
        if not self.head:
            self.addAtHead(val)
        else:
            while current.next:
                current = current.next
            current.next = new_node
            self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            return -1
        elif index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            counter = 0
            while counter < index-1:
                counter += 1
                current = current.next
            next_node = current.next
            new_node = self.Node()
            new_node.set_item(val)
            new_node.next = next_node
            current.next = new_node
        self.length += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return -1
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            counter = 0
            while counter < index-1:
                counter += 1
                current = current.next
            if not current.next:
                return -1
            current.next = current.next.next
        self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



# class MyLinkedList:

#     def __init__(self):
#         self.list = []
#         self.length = 0
#     def get(self, index: int) -> int:
#         if index >= self.length or self.length == 0:
#             return -1 
#         else:
#             return self.list[index]
#     def addAtHead(self, val: int) -> None:
#         if self.length == 0:
#             self.list.append(val)
#             self.length += 1
#         else:
#             self.list.insert(0,val)
#             self.length += 1
#     def addAtTail(self, val: int) -> None:
#         self.list.append(val)
#         self.length += 1
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.length:
#             return -1
#         else:
#             self.list.insert(index,val)
#             self.length += 1
#     def deleteAtIndex(self, index: int) -> None:
#         if self.length == 0 or index >= self.length:
#             return - 1
#         self.list.pop(index)
#         self.length -= 1
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)
