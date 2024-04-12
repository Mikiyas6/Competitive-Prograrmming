# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:

            return head

        current = head
        size = 0

        while current:

            current = current.next
            size += 1

        k = k%size
        if k == 0:

            return head
        end_up = size - k - 1
        current = head

        for i in range(end_up):
            current = current.next
        
        rotated_part = current.next
        current.next = None

        current = rotated_part

        while current.next:

            current = current.next
        
        current.next = head

        return rotated_part

