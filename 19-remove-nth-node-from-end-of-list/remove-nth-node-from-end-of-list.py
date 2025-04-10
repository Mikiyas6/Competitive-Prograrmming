# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        end_up = size - n - 1
        if end_up < 0:
            return head.next
        current = head
        for _ in range(end_up):
            current = current.next
        current.next = current.next.next
        return head