# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def find_length(head):

            current = head
            size = 0

            while current:

                size += 1
                current = current.next
            
            return size

        size_A = find_length(headA)
        size_B = find_length(headB)

        if size_A > size_B:

            current1 = headA
            current2 = headB
        
        else:
        
            current1 = headB
            current2 = headA

        end_up = abs(size_A-size_B)

        for i in range(end_up):

            current1 = current1.next
        
        while current1 != current2:

            current1 = current1.next
            current2 = current2.next
        
        return current1