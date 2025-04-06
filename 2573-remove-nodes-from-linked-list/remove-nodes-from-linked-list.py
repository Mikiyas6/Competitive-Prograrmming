# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            while stack and current.val > stack[-1]:
                stack.pop()
            stack.append(current.val)
            current = current.next
        dummy = ListNode(-1)
        current = dummy
        for i in range(len(stack)):
            current.next = ListNode(stack[i])
            current = current.next
        return dummy.next