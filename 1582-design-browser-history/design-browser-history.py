# Definition for singly-linked list.
class ListNode:
    def __init__(self, val="", next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.head = ListNode(homepage)
        self.tail = self.head
        self.current = self.head

    def visit(self, url: str) -> None:
        
        Node = ListNode(url)
        Node.prev = self.current
        self.current.next = Node
        self.current = self.current.next
        self.tail = self.current

    def back(self, steps: int) -> str:
        

        for _ in range(steps):

            if not self.current.prev:
                return self.current.val
            self.current = self.current.prev
        
        return self.current.val

    def forward(self, steps: int) -> str:
        
        for _ in range(steps):

            if not self.current.next:
                return self.current.val
            self.current = self.current.next
        
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)