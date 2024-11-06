# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head

        if left == right:
            return head
        
        def reverse(head):

            if not head.next:
                return head
            
            right_part = head.next
            head.next = None
            node = head
            reversedList = reverse(right_part)
            current = reversedList

            while current.next:
                current = current.next
            
            current.next = node
            return reversedList

        if left == 1:
            first_part = None
            second_part = head

        elif left == 2:
            second_part = head.next
            head.next = None
            first_part = head

        else:
            left_end_up = left-2
            current = head
            for i in range(left_end_up):
                current = current.next
            second_part = current.next
            current.next = None
            first_part = head
        
        
        if not second_part:
            return first_part
        right_end_up = right-left
        current = second_part
        for _ in range(right_end_up):
            current = current.next
        last_part = current.next
        current.next = None
        to_be_reversed = second_part

        if not to_be_reversed:
            return head
        reversedList = reverse(to_be_reversed)
        current = first_part
        if current:
            while current.next:
                current = current.next
            current.next = reversedList
        current = reversedList
        while current.next:
            current = current.next
        current.next = last_part

        return first_part if first_part else reversedList

