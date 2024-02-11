# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
    
        # Phase 1: Find the meeting point to know wether there's a cycle or not
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        # If there is no cycle
        if slow != fast:
            return None
        
        # Phase 2: Find the start of the cycle
        slow = head
        
        while slow != fast:

            slow = slow.next
            fast = fast.next

        return slow
