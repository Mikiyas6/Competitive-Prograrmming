# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True
        
        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head):
            prev = None  
            current = head 
            while current:
                next_node = current.next 
                current.next = prev 
                prev = current 
                current = next_node 
            return prev 

        middle = findMiddle(head)
        second_part = middle.next
        middle.next = None
        first_part = head
        reversed_second_part = reverse(second_part)
        ptr1 = first_part
        ptr2 = reversed_second_part
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True 