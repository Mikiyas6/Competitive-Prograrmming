# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # def findMiddle(head):
        #     if not head or not head.next:
        #         return head
        #     slow = head
        #     fast = head
        #     while fast and fast.next:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return slow
       
        # middle = findMiddle(head) 
        # last_part = middle.next
        # middle.next = None
        # stack = []
        # while last_part:
        #     stack.append(last_part)
        #     last_part = last_part.next
        # current = head
        # while current and stack:
        #     next = current.next
        #     node = stack.pop()
        #     current.next = node
        #     node.next = next
        #     current = next
        def findMiddle(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse(head):
            prev = None
            current = head
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        middle = findMiddle(head)
        last_part = middle.next
        middle.next = None
        reversed_last_part = reverse(last_part)
        ptr1 = head
        ptr2 = reversed_last_part
        current = None
        def helper(ptr1,ptr2):
            if not ptr1:
                return ptr2
            if not ptr2:
                return ptr1
            if not ptr1 and not ptr2:
                return None
            next1 = ptr1.next
            next2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = helper(next1,next2)
            return ptr1
        helper(head,reversed_last_part)

