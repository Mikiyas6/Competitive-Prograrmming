# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        current = dummy
        while head and head.next:
            current.next = ListNode(head.next.val)
            current = current.next
            current.next = ListNode(head.val)
            current = current.next
            head = head.next.next
        if head:
            current.next = head
        return dummy.next