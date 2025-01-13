# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        current1, current2 = dummy1, dummy2
        current = head
        def fun(current1,current2,current,x):
            if not current:
                current = dummy1
                while current.next:
                    current = current.next
                current.next = dummy2.next
                return dummy1.next
            if current.val < x:
                current1.next = ListNode(current.val)
                current1 = current1.next
            else:
                current2.next = ListNode(current.val)
                current2 = current2.next
            return fun(current1,current2,current.next,x)
        
        return fun(current1,current2,current,x)
