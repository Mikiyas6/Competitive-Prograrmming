# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head
        
        def fun(ptr):

            if not ptr or not ptr.next:

                return ptr
            
            second_part = ptr.next.next

            ptr.next.next = None

            second_node = ptr.next

            ptr.next = None

            first_node = ptr

            second_node.next = first_node

            current = second_node

            while current.next:

                current = current.next
            
            current.next = fun(second_part)

            return second_node
        
        return fun(head)