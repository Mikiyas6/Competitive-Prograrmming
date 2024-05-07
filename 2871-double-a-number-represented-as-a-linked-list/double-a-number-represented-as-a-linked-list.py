# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev

        # Double the linked list
        current = head
        carry = 0
        while current or carry:
            if not current:
                current = ListNode(0)
                prev.next = current
            total = current.val * 2 + carry
            current.val = total % 10
            carry = total // 10
            prev, current = current, current.next

        # Reverse the linked list again
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev

        return head