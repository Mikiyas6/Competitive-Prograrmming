# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy = ListNode(-1)

#         while head:

#             current = dummy
#             prev = current

#             while current:
#                 if head.val < current.val:

#                     node = ListNode(head.val)
                    
#                     if prev == current:
#                         temp = prev
#                         node.next = prev.next
#                         prev.next = node
#                     else:

#                         prev.next = node
#                         node.next = current

#                     break
                
#                 prev = current 
#                 current = current.next
            
#             if not current:

#                 node = ListNode(head.val)
#                 prev.next = node
            
#             head = head.next
        
#         return dummy.next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Find the middle of the linked list
        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None  # Break the list into two halves
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def find_middle(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, l1, l2):
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
        
        current.next = l1 or l2
        
        return dummy.next
