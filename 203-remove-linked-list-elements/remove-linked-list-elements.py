# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        def helper(current,head,val):
            if not head:
                return current
            if head.val != val:
                node = ListNode(head.val)
                current.next = helper(node,head.next,val)
                return current
            return helper(current,head.next,val)
        return helper(current,head,val).next

            