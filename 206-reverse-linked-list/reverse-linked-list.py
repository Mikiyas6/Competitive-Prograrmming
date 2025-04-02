# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if not head or not head.next:
                return head
            right = head.next
            head.next = None
            left = head
            reversed_right_part = reverse(right)
            current = reversed_right_part
            while current.next:
                current = current.next
            current.next = left
            return reversed_right_part
        
        return reverse(head)