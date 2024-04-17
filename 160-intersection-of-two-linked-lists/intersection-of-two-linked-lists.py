# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        current = headA
        size_A = 0 

        while current:
            size_A += 1
            current = current.next
        
        size_B = 0
        current = headB

        while current:

            size_B += 1
            current = current.next

        if size_A > size_B:

            end_up = size_A-size_B
            current1 = headA
            current2 = headB
        
        else:
            
            end_up = size_B-size_A
            current1 = headB
            current2 = headA
            
        for i in range(end_up):

            current1 = current1.next
        
        while current1 != current2:

            current1 = current1.next
            current2 = current2.next
        
        return current1
        

        # current = headA

        # while current.next:

        #     current = current.next
        
        # current.next = headB
        
        # slow = headA
        # fast = headA

        # while fast and fast.next:

        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:

        #         break
        
        # if not fast or not fast.next:

        #     return None
        
        # slow = headA

        # while slow != headA:

        #     slow = slow.next
        #     fast = fast.next
        
        # return slow