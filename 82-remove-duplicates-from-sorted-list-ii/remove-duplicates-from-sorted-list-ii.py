# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        dummy = ListNode(-1)
        current = dummy

        def fun(current,ptr1,ptr2,visited):

            if not ptr2:

                if ptr1.val not in visited:

                    Node = ListNode(ptr1.val)

                    current.next = Node
                
                return current
            
            if ptr1.val != ptr2.val:

                if ptr1.val not in visited:

                    Node = ListNode(ptr1.val)
                    visited.add(ptr1.val)
                    current.next = fun(Node,ptr1.next,ptr2.next,visited)

                    return current

            visited.add(ptr1.val)
            return fun(current,ptr1.next,ptr2.next,visited)

        return fun(current,head,head.next,set()).next




        