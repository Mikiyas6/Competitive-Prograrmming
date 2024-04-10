# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:

            return head

        # finding the size

        size = 0
        ptr = head

        while ptr:

            size += 1
            ptr = ptr.next
        
        k %= size

        if k == 0:

            return head
        
        end_up = size - k - 1

        ptr = head

        for _ in range(end_up):

            ptr = ptr.next
        
        rotated_part = ptr.next
        ptr.next = None
        first_part = head

        current = rotated_part

        while current.next:

            current = current.next
        
        current.next = first_part

        return rotated_part
        
        
