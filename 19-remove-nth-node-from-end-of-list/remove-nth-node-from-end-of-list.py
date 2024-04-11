# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Calculate the size

        current = head
        size = 0

        while current:

            current = current.next
            size += 1
        
        # Removing the nth node
        end_up = size - n - 1
        if end_up < 0:
            head = head.next
            return head
            
        current = head

        for i in range(end_up):

            current = current.next
        
        current.next = current.next.next

        return head
