# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        def makeCopy(head):
            dummy = ListNode(-1)
            current = dummy
            ptr = head
            while ptr:
                current.next = ListNode(ptr.val)
                ptr = ptr.next
                current = current.next
            return dummy.next
        
        ptr1 = head
        ptr2 = reverse(makeCopy(head))
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True if (not ptr1 and not ptr2) else False