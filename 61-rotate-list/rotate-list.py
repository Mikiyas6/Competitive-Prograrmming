# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            current = head

            while current:
                next_node = current.next  
                current.next = prev       
                prev = current            
                current = next_node       

            return prev  
       
        if not head or not head.next:
            return head
        n = 0
        current = head
        while current:
            current = current.next
            n += 1
        k %= n
        end_up = n - k - 1
        current = head
        for i in range(end_up):
            current = current.next
        second_part = current.next
        current.next = None
        first_part = head
        reversed_first_part = reverse(first_part)
        reversed_second_part = reverse(second_part)
        current = reversed_first_part
        while current.next:
            current = current.next
        current.next = reversed_second_part
        final_result = reverse(reversed_first_part)
        return final_result
        