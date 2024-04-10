# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def fun(head): #To reverse a list

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

        if not head or not head.next:

            return head
        
        # Break the linkedlist in half

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        first_half = head

        # Reverse the second half
        reversed_second_half = fun(second_half)

        ptr1 = head
        ptr2 = reversed_second_half

        while ptr1 and ptr2:
            next_ptr1 = ptr1.next
            next_ptr2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = next_ptr1

            ptr1 = next_ptr1
            ptr2 = next_ptr2
        
        # combine one element from each half
        # ptr1 = first_half
        # ptr2 = reversed_second_half

        # dummy = ListNode(-1)
        # current = dummy

        # flag = True

        # while ptr1 and ptr2:

        #     if flag:

        #         value = ptr1.val
        #         ptr1 = ptr1.next
        #         flag = False
            
        #     else:

        #         value = ptr2.val
        #         ptr2 = ptr2.next
        #         flag = True
            
        #     Node = ListNode(value)
        #     current.next = Node
        #     current = current.next
        
        # if not ptr1:

        #     current.next = ptr2
        
        # else:

        #     current.next = ptr1
        
        # linked_list = dummy.next
        # print(linked_list)

        




        
        