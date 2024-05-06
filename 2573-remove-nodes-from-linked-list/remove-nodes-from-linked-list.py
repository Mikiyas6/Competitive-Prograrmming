# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        mono_stack = []
        current = head

        while current:
            second_half = current.next
            current.next = None
            first_node = current

            while mono_stack and (mono_stack[-1]).val < current.val:
                mono_stack.pop()
            
            mono_stack.append(current)
            current = second_half
        
        dummy = ListNode(-1)
        current = dummy

        while mono_stack:
            current.next = mono_stack.pop(0)
            current = current.next
        
        result = dummy.next
        return result