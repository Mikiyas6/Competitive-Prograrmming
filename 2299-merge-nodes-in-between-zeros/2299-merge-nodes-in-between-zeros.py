# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        temp = head.next
        
        while temp:
            sum_val = 0
            while temp and temp.val != 0:
                sum_val += temp.val
                temp = temp.next
            
            current.next = ListNode(sum_val)
            current = current.next
            
            if temp:
                temp = temp.next
        
        return dummy.next