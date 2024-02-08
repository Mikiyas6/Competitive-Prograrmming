class MyLinkedList:

    class Node:

        def __init__(self,val):

            self.val = val
            self.next = None
        
        def set_value(self,val):

            self.val = val
        
        def get_value(self):

            return self.val
        
        def set_next(self,next):

            self.next = next
        
        def get_next(self):

            return self.next

    def __init__(self):

        self.head = None
        self.size = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:

            return -1
        
        current = self.head

        for i in range(index):

            current = current.next
        
        return current.val
    
    def get_node(self, index: int) -> Node:

        if index < 0 or index >= self.size:

            return None
        
        current = self.head

        for i in range(index):

            current = current.next

        return current
        
    def addAtHead(self, val: int) -> None:
        
        new_node = self.Node(val)

        new_node.next = self.head

        self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:

        new_node = self.Node(val)
        
        current = self.head

        if not current:

            return self.addAtHead(val)

        while current.next:

            current = current.next
        
        current.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:

            return self.addAtHead(val)
        
        elif index == self.size:

            return self.addAtTail(val)
        
        else:

            prev = self.get_node(index-1)

            if prev is None or prev.next is None:
                return  # Invalid index or prev node is None

            temp = prev.next

            new_node = self.Node(val)

            prev.next = new_node

            new_node.next = temp
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return  None

        if index == 0:
            return self.deleteAtHead()

        if index == self.size - 1:
            return self.deleteAtTail()

        prev = self.get_node(index - 1)
        if prev is None or prev.next is None:
            return  # Invalid index or prev node is None

        prev.next = prev.next.next
        self.size -= 1

    def deleteAtHead(self) -> None:

        self.head = self.head.next

        self.size -= 1
    
    def deleteAtTail(self) -> None:

        if self.size == 0:

            return None

        if self.size == 1:

            return self.deleteAtHead()

        index = self.size - 2

        prev = self.get_node(index)

        prev.next = None
    
        self.size -= 1
    
    def get_size(self) -> None:

        return self.size



    


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
