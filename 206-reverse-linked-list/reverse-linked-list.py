# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def fun(head):

            if not head or not head.next:

                return head

            second_part = head.next

            head.next = None

            first_node = head
            
            reversed_linked_list = fun(second_part)

            head = reversed_linked_list

            current = head

            while current.next:

                current = current.next

            current.next = first_node

            return reversed_linked_list
        
        return fun(head)