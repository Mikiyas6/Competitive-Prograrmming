# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy

        if not head or not head.next:

            return head

        ptr1 = head
        ptr2 = head.next

        while ptr2:

            if ptr1.val != ptr2.val:

                Node = ListNode(ptr1.val)
                current.next = Node
                current = current.next
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        Node = ListNode(ptr1.val)
        current.next = Node

        return dummy.next 
        
