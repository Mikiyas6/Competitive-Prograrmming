# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        def fun(head): #To reverse a list

            prev = None
            current = head

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev
        
        dummy = ListNode(-1)
        current = dummy

        end_up = k - 1

        ptr = head
        second_part = None

        while ptr:

            for i in range(end_up):

                ptr = ptr.next

                if not ptr:

                    current.next = second_part
                    return dummy.next
            
            second_part = ptr.next
            ptr.next = None

            reversed_part = fun(head)

            current.next = reversed_part

            while current.next:

                current = current.next
            
            ptr = second_part
            head = second_part
        
        return dummy.next

