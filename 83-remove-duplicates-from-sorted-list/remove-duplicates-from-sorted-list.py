# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(-101)
        # current = dummy
        # def removeDuplicates(current,root):
        #     if not root:
        #         return current
        #     if current.val != root.val:
        #         node = ListNode(root.val)
        #         current.next = removeDuplicates(node,root.next)
        #         return current
        #     return removeDuplicates(current,root.next)
        # return removeDuplicates(current,head).next
        dummy = ListNode(-101)
        current = dummy
        while head:
            if head.val != current.val:
                node = ListNode(head.val)
                current.next = node
                current = node
            head = head.next
        return dummy.next
