# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head

        def fun(left, right, head, x):
            if not head.next:
                if head.val < x:
                    left.next = ListNode(head.val)
                else:
                    right.next = ListNode(head.val)
                return left.next, right.next

            if head.val < x:
                left.next = ListNode(head.val)
                return fun(left.next, right, head.next, x)
            else:
                right.next = ListNode(head.val)
                return fun(left, right.next, head.next, x)

        dummy_left = ListNode(-1)
        dummy_right = ListNode(-1)
        left, right = fun(dummy_left, dummy_right, head, x)

        current = dummy_left
        while current.next:
            current = current.next
        current.next = dummy_right.next

        return dummy_left.next