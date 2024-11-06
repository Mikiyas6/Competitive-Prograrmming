# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            current = head

            while current:
                next_node = current.next  
                current.next = prev       
                prev = current            
                current = next_node       

            return prev 

        if not head:
            return head
        current = head
        n = 0
        while current:
            current = current.next
            n += 1
        end_up = n-(n%k)-1
        current = head
        for i in range(end_up):
            current = current.next
        unreversed_part = current.next
        current.next = None

        end_up = k - 1
        current = head
        ptr = current

        def fun(ptr):
            if not ptr:
                return ptr
            current = ptr
            for i in range(end_up):
                current = current.next
            second_part = current.next
            current.next = None
            reversedList = reverse(ptr)
            current = reversedList
            while current.next:
                current = current.next
            current.next = fun(second_part)
            return reversedList
        
        properly_reversed = fun(ptr)
        current = properly_reversed
        while current.next:
            current = current.next
        current.next = unreversed_part
        return properly_reversed

            


            
