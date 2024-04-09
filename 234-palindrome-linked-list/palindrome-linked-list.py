# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def fun(head):

            prev = None
            current = head

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        # def fun(head):

        #     if not head or not head.next:

        #         return head
            
        #     second_part = head.next
        #     head.next = None
        #     first_node = head

        #     reversed_second_part = fun(second_part)

        #     current = reversed_second_part

        #     while current.next:

        #         current = current.next
            
        #     current.next = first_node

        #     return reversed_second_part

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

        # Check the whether the two parts are equal or not. If they are then it's palindromic
        ptr1 = first_half
        ptr2 = reversed_second_half

        while ptr1 and ptr2:

            if ptr1.val != ptr2.val:

                return False
        
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return True

        




    