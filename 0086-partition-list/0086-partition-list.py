# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_left = ListNode(-1)
        dummy_right = ListNode(-1)
        ptr1 = dummy_left
        ptr2 = dummy_right
        current = head
        while current:
            if current.val < x:
                ptr1.next = ListNode(current.val)
                ptr1 = ptr1.next
            else:
                ptr2.next = ListNode(current.val)
                ptr2 = ptr2.next
            current = current.next
        current = dummy_left
        while current.next:
            current = current.next
        current.next = dummy_right.next
        return dummy_left.next