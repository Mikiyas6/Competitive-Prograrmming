# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy
        def merge(current,ptr1,ptr2):
            if not ptr1:
                current.next = ptr2
                return current
            if not ptr2:
                current.next = ptr1
                return current
            if ptr1.val <= ptr2.val:
                value = ptr1.val
                ptr1 = ptr1.next
            else:
                value = ptr2.val
                ptr2 = ptr2.next
            node = ListNode(value)
            current.next = merge(node,ptr1,ptr2)
            return current
        return merge(current,list1,list2).next