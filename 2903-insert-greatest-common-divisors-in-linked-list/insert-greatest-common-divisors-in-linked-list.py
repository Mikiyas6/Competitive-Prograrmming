# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        while current.next:
            gcd_val = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_val, current.next)
            current.next = new_node
            current = current.next.next

        return head