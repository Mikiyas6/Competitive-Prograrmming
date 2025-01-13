# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or not head.next or left == right:
            return head
        
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        dummy1,dummy2,dummy3 = ListNode(-1),ListNode(-1),ListNode(-1)
        current1,current2,current3 = dummy1,dummy2,dummy3

        counter = 1
        current = head
        while current:
            value = ListNode(current.val)
            if counter < left:
                current1.next = value
                current1 = current1.next
            elif counter >= left and counter <= right:
                current2.next = value
                current2 = current2.next
            else:
                current3.next = value
                current3 = current3.next
            counter += 1
            current = current.next
        
        reversed_part = reverse(dummy2.next)
        current = dummy1
        while current.next:
            current = current.next
        current.next = reversed_part
        current = reversed_part
        while current.next:
            current = current.next
        current.next = dummy3.next
        return dummy1.next
        