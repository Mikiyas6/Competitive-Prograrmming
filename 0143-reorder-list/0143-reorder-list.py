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
        def find_middle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        middle = find_middle(head)
        second_half = middle.next
        middle.next = None
        ptr1 = head
        ptr2 = reverse(second_half)
        def fun(ptr1,ptr2):
            if not ptr1 and not ptr2:
                return None
            if not ptr2 and ptr1:
                return ptr1
            next1 = ptr1.next
            next2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = fun(next1,next2)
            return ptr1
        fun(ptr1,ptr2)

