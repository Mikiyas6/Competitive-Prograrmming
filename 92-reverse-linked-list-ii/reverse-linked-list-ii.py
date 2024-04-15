# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        def fun(head):

            if not head or not head.next:

                return head
            
            second_part = head.next
            head.next = None
            first_node = head

            reversed_second_part = fun(second_part)

            current = reversed_second_part

            while current.next:

                current = current.next
            
            current.next = first_node

            return reversed_second_part

        current =  head
        end_up = left - 2

        if end_up >= 0:

            for i in range(end_up):

                current = current.next
            
            second_part = current.next
            current.next = None
            
            first_part = head # The first part

        else:

            second_part = head
            first_part = None

        current = second_part
        calibrated = right - left

        for i in range(calibrated):

            current = current.next

        if current:
            last_part = current.next  # The last part
            current.next = None
        
        else:

            last_part = None

        middle_part = second_part # The part we want to reverse

        reversed_middle_part = fun(middle_part)

        if first_part:

            current = first_part

            while current.next:

                current = current.next

            current.next = reversed_middle_part
        
        else:

            first_part = reversed_middle_part

        current = reversed_middle_part
        while current.next:

            current = current.next

        current.next = last_part

        return first_part


