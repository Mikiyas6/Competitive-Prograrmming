# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        value1 = None
        for _ in range(k-1):
            current = current.next
        value1 = current.val
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        value2 = slow.val
        slow.val = value1
        current = head
        for _ in range(k-1):
            current = current.next
        current.val = value2
        return head

