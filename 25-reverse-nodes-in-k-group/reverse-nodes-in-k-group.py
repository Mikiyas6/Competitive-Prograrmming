# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        end_up = k - 1

        def reverse(ptr):

            if not ptr or not ptr.next:

                return ptr
            
            second_part = ptr.next

            ptr.next = None
        
            first_node = ptr

            reversed_second_part = reverse(second_part)

            current = reversed_second_part

            while current.next:

                current = current.next
            
            current.next = first_node

            return reversed_second_part

        def fun(ptr):

            if not ptr or not ptr.next:

                return ptr
            
            uncut = ptr
            
            for i in range(end_up):

                ptr = ptr.next

                if not ptr:
                    return uncut

            second_part = ptr.next
            ptr.next = None

            reversed_first_part = reverse(uncut)

            current = reversed_first_part

            while current.next:

                current = current.next
            
            current.next = fun(second_part)
            
            return reversed_first_part
        
        return fun(head)


            
