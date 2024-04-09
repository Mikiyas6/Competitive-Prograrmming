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

            second_part_reversed = fun(second_part)

            head = second_part_reversed

            current = head

            while current.next:
                current = current.next

            current.next = first_node

            return head

        end_up = left - 2

        if right - left <= 0:
            return head

        if left == 1:
            first_part = None
            second_half = head
        else:
            current = head
            for _ in range(end_up):
                current = current.next
            second_half = current.next
            current.next = None
            first_part = head

        end_up = right - left
        current = second_half
        for _ in range(end_up):
            current = current.next

        last_part = current.next
        current.next = None
        middle = second_half

        middle_reversed = fun(middle)

        current = first_part
        if not first_part:
            current = middle_reversed

        while current.next:
            current = current.next

        if not first_part:
            current.next = last_part
            return middle_reversed

        current.next = middle_reversed

        while current.next:
            current = current.next

        current.next = last_part

        return first_part

        # if not head or not head.next:

        #     return head
        
        # def fun(head):

        #     if not head or not head.next:

        #         return head
            
        #     second_part = head.next
        #     head.next = None

        #     first_node = head

        #     second_part_reversed = fun(second_part)

        #     head = second_part_reversed

        #     current = head

        #     while current.next:

        #         current = current.next
            
        #     current.next = first_node

        #     return head
        
        # end_up = left - 2

        # if right - left <= 0:

        #     return head 

        # if left == 1:

        #     first_part = None
        #     second_half = head
        # else:
        #     current = head

        #     for i in range(end_up):

        #         current = current.next
            
        #     second_half = current.next
        #     current.next = None
        #     first_part = head
            
        # end_up = right-left
        # current = second_half

        # for i in range(end_up):

        #     current = current.next

        # last_part = current.next
        # current.next = None
        # middle = second_half
        
        # middle_reversed = fun(middle)

        # current = first_part

        # if not first_part:

        #     current = middle_reversed

        # while current.next:

        #     current = current.next
        
        # if not first_part:

        #     current.next = last_part

        #     return middle_reversed
        
        # current.next = middle_reversed

        # while current.next:

        #     current = current.next
        
        # current.next = last_part

        # return first_part
