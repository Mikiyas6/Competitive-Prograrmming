# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         if not head or not head.next:
#             return head

#         size = 0
#         current = head
#         while current:
#             size += 1
#             current = current.next
        
#         end_up_1 = k - 2
#         end_up_2 = size-k-1

#         if end_up_1 == end_up_2:
#             return head
        
#         if end_up_2 < end_up_1:

#             temp = end_up_2
#             end_up_2 = end_up_1
#             end_up_1 = temp
        
#         current = head
#         for i in range(end_up_1):
#             current = current.next
        
#         second_part = current.next
#         current.next = None
#         first_part = head
#         middle_part = second_part.next
#         second_part.next = None
#         first_node = second_part

#         current = middle_part
#         new_ending = end_up_2-end_up_1-2
#         if new_ending < 1:
#             third_part = current.next
#             current.next = None
#             second_node = middle_part
            
#         else:
#             for i in range(new_ending):
#                 current = current.next
            
#             third_part = current.next
#             current.next = None
#             second_node = middle_part
#             last_part = third_part.next
#             third_part.next = None

#         current = first_part

#         while current.next:
#             current = current.next
        
#         current.next = second_node
#         current = current.next

#         current.next = middle_part

#         while current.next:
#             current = current.next
        
#         current.next = first_node
#         current = current.next

#         current.next = last_part
    
#         return first_part

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        
        end_up_1 = k
        end_up_2 = size - k + 1

        if end_up_1 == end_up_2:
            return head

        if end_up_2 < end_up_1:
            end_up_1, end_up_2 = end_up_2, end_up_1

        first_prev, second_prev = None, None
        current = head
        for i in range(end_up_1 - 1):
            first_prev = current
            current = current.next
        
        first_node = current

        current = head
        for i in range(end_up_2 - 1):
            second_prev = current
            current = current.next
        
        second_node = current

        if first_prev:
            first_prev.next = second_node
        else:
            head = second_node

        if second_prev:
            second_prev.next = first_node
        else:
            head = first_node

        first_node.next, second_node.next = second_node.next, first_node.next

        return head
