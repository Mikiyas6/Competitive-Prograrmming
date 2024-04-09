# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()
        
        if not head or not head.next:

            return head

        dummy = ListNode(-1)
        current = dummy
        
        ptr1 = head
        ptr2 = head.next

        while ptr2:

            if ptr1.val == ptr2.val:
                visited.add(ptr1.val)
                ptr1 = ptr1.next.next
                if not ptr1:
                    return dummy.next
                ptr2 = ptr2.next.next
            
            else:

                if ptr1.val not in visited:
                    Node = ListNode(ptr1.val)
                    current.next = Node
                    current = current.next
                visited.add(ptr1.val)
                ptr1 = ptr1.next
                ptr2 = ptr2.next

        if ptr1.val not in visited:  
            Node = ListNode(ptr1.val)
            current.next = Node
        return dummy.next
            