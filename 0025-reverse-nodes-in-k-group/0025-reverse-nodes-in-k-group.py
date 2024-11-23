# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def reverse(head):
            if not head.next:
                return head
            secondPart = head.next
            head.next = None
            reversedPart = reverse(secondPart)
            current = reversedPart
            while current.next:
                current = current.next
            current.next = head
            return reversedPart
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        end_up = size-(size%k)-1
        current = head
        for _ in range(end_up):
            current = current.next
        unReversedPart = current.next
        current.next = None
        def fun(head,ptr):
            if not head:
                return head
            for i in range(k-1):
                ptr = ptr.next
            secondPart = ptr.next
            ptr.next = None
            reversed_part = reverse(head)
            current = reversed_part
            while current.next:
                current = current.next
            ptr = secondPart
            current.next = fun(secondPart,ptr)
            return reversed_part
        current = head
        reversed_part = fun(head,current)
        current = reversed_part
        while current.next:
            current = current.next
        current.next = unReversedPart
        return reversed_part
       
        