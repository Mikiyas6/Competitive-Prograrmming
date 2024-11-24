# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(-1)
        current = dummy
        ptr = head
        while ptr:
            if ptr.val != val:
                current.next = ListNode(ptr.val)
                current = current.next
            ptr = ptr.next
        return dummy.next