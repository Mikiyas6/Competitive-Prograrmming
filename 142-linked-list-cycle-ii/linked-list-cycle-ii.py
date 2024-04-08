# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                break
        
        if not fast or not fast.next:

            return None
        
        ptr1 = head
        ptr2 = fast

        while ptr1 != ptr2:

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1