# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        ptr = head
        while ptr:
            total = 0
            while ptr.val != 0:
                total += ptr.val
                ptr = ptr.next
            if total:
                node = ListNode(total)
                current.next = node
                current = current.next
            ptr = ptr.next
        return dummy.next

            