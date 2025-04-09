# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            if not head or not head.next:
                return head
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        
        middle = findMiddle(head)
        second_part = middle.next
        middle.next = None
        reversed_second_part = reverse(second_part)

        ptr1 = head
        ptr2 = reversed_second_part
        max_sum = float('-inf')
        while ptr1 and ptr2:
            total = ptr1.val + ptr2.val
            max_sum = max(max_sum,total)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return max_sum
