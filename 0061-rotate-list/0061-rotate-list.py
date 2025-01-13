# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        end_up = size-(k%size)- 1
        current = head
        for _ in range(end_up):
            current = current.next
        second_half = current.next
        current.next = None
        first_half = head
        reversed_first_half = reverse(first_half)
        reversed_second_half = reverse(second_half)
        current = reversed_first_half
        while current.next:
            current = current.next
        current.next = reversed_second_half
        result = reverse(reversed_first_half)
        return result