# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
       
        middle = findMiddle(head) 
        last_part = middle.next
        middle.next = None
        stack = []
        while last_part:
            stack.append(last_part)
            last_part = last_part.next
        current = head
        while current and stack:
            next = current.next
            node = stack.pop()
            current.next = node
            node.next = next
            current = next

