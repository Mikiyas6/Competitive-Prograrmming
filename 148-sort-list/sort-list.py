# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_sort(left,right):
            dummy = ListNode(-1)
            current = dummy
            def fun(current,left,right):
                if not left:
                    current.next = right
                    return current
                if not right:
                    current.next = left
                    return current
                if left.val <= right.val:
                    node = ListNode(left.val)
                    left = left.next
                else:
                    node = ListNode(right.val)
                    right = right.next
                current.next = fun(node,left,right)
                return current
            return fun(current,left,right).next

        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def split(head):
            if not head or not head.next:
                return head
            middle = findMiddle(head)
            right_side = middle.next
            middle.next = None
            left_side = head
            left = split(left_side)
            right = split(right_side)
            merged = merge_sort(left,right)
            return merged
        
        return split(head)
