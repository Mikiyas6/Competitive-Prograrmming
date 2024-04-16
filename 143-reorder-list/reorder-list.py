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

        if not head or not head.next:

            return head
        
        def get_middle(head):

            slow = head
            fast = head.next

            while fast and fast.next:

                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(head):

            if not head or not head.next:

                return head
            
            second_part = head.next
            head.next = None
            first_node = head

            reversed_second_part = reverse(second_part)

            current = reversed_second_part

            while current.next:
                
                current = current.next
            
            current.next = first_node

            return reversed_second_part
        
        def merge(first_part,second_part):

            if not first_part:

                return None
            
            if not second_part:

                first_part.next = second_part

                return first_part

            rest_of_first_part = first_part.next
            first_part.next = None
            rest_of_second_part = second_part.next
            second_part.next = None

            first_part.next = second_part

            second_part.next = merge(rest_of_first_part,rest_of_second_part) 

            return first_part

        middle_node = get_middle(head)

        second_part = middle_node.next
        middle_node.next = None

        first_part = head

        reversed_second_part = reverse(second_part)

        merge(first_part,reversed_second_part)
