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
            while fast.next:
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
        middle = findMiddle(head)
        second_part = middle.next
        middle.next = None
        reversed_second_part = reverse(second_part)
        first_part = head
        current1 = reversed_second_part
        current2 = first_part
        maxSum = 0
        while current1:
            total = current1.val + current2.val
            maxSum = max(maxSum,total)
            current1 = current1.next
            current2 = current2.next
        return maxSum