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
            second_part = head.next
            head.next = None
            reversed_second_part = reverse(second_part)
            current = reversed_second_part
            while current.next:
                current = current.next
            current.next = head
            return reversed_second_part
        
        return reverse(head)