# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Adjust k to be within the length of the linked list
        k %= length
        if k == 0:
            return head

        # Find the new tail and break the list
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        # Attach the original tail to the original head to form a circle
        tail.next = head

        return new_head
        
        # if not head or not head.next or k == 0:

        #     return head
        
        # ptr = head

        # size = 0

        # while ptr:

        #     size += 1
        #     ptr = ptr.next
        
        # ptr = head
        # end_up = k

        # if size %2 == 0:
        #     end_up -= 1
        
        # def fun(head):

        #     prev = None
        #     current = head

        #     while current:
        #         next_node = current.next
        #         current.next = prev
        #         prev = current
        #         current = next_node

        #     return prev

        # for i in range(end_up):

        #     ptr = ptr.next

        #     if not ptr:
        #         ptr = head

        # second_part = ptr.next
        # ptr.next = None

        # reversed_second_part = fun(second_part)
        # reversed_first_part = fun(head)

        # current = reversed_first_part

        # while current.next:

        #     current = current.next
        
        # current.next = reversed_second_part

        # return fun(reversed_first_part)
