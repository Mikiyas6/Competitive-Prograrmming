# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        current = dummy
        ptr1 = head
        ptr2 = head.next
        def remover(current,ptr1,ptr2,flag):
            if not ptr2:
                if ptr1.val != flag:
                    node = ListNode(ptr1.val)
                    current.next = node
                return current
            if ptr1.val != ptr2.val:
                if ptr1.val != flag:
                    node = ListNode(ptr1.val)
                else:
                    return remover(current,ptr1.next,ptr2.next,flag)
            else:
                flag = ptr1.val
                return remover(current,ptr1.next,ptr2.next,flag)
            current.next = remover(node,ptr1.next,ptr2.next,flag)
            return current
        return remover(current,ptr1,ptr2,-101).next
