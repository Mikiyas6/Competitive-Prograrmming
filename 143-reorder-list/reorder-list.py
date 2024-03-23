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
            return

        # Step 1: Split the linked list into two halves
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None  # Split the list

        # Step 2: Reverse the second half of the linked list
        prev = None
        current = second_half
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        second_half = prev

        # Step 3: Merge the two halves by interweaving the nodes
        p1 = head
        p2 = second_half
        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
        