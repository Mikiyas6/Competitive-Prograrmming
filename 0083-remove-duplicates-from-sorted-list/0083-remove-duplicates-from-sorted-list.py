# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        dummy = ListNode(-1)
        current = dummy
        ptr1 = head
        ptr2 = head.next

        def removeDuplicates(current,ptr1,ptr2):

            if not ptr2:
                node = ListNode(ptr1.val)
                current.next = node
                return current

            if ptr1.val != ptr2.val:
                node = ListNode(ptr1.val)
                current.next = removeDuplicates(node,ptr1.next,ptr2.next)
                return current
            
            return removeDuplicates(current,ptr1.next,ptr2.next)
        
        return removeDuplicates(current,ptr1,ptr2).next