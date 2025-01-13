# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_middle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left,right):
            ptr1 = left
            ptr2 = right
            dummy = ListNode(-1)
            current = dummy
            def merger(current,ptr1,ptr2):
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
                current.next = merger(node,ptr1,ptr2)
                return current
            return merger(current,ptr1,ptr2).next
        
        def fun(head):
            if not head or not head.next:
                return head
            middle = find_middle(head)
            right = middle.next
            middle.next = None
            left = head
            left_side = fun(left)
            right_side = fun(right)
            merged = merge(left_side,right_side)
            return merged
        
        return fun(head)
        
            