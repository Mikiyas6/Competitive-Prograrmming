# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        ptr1, ptr2 = dummy1, dummy2

        def fun(ptr1,ptr2,head):

            if not head:

                return

            if not head.next:

                ptr1.next = head

                return 
            
            second_part = head.next
            head.next = None
            first_node = head

            next_second_part = second_part.next
            second_part.next = None
            second_node = second_part

            ptr1.next = first_node
            ptr2.next = second_node
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            fun(ptr1,ptr2,next_second_part)
        
        fun(ptr1,ptr2,head)

        first_part = dummy1.next
        second_part = dummy2.next

        current = first_part

        while current.next:

            current = current.next
        
        current.next = second_part

        return first_part

