# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy
        ptr1,ptr2,carry = l1,l2,0

        def fun(current,ptr1,ptr2,carry):

            if not ptr1 and not ptr2:

                if carry > 0:

                    Node = ListNode(carry)

                    current.next = Node

                return current
            
            if not ptr2:

                total = ptr1.val + carry
                ptr1 = ptr1.next
            
            elif not ptr1:

                total = ptr2.val + carry
                ptr2 = ptr2.next
            
            else:
            
                total = ptr1.val + ptr2.val + carry
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            result = total % 10
            carry = total // 10

            Node = ListNode(result)

            current.next = fun(Node,ptr1,ptr2,carry)

            return current
        
        return fun(current,ptr1,ptr2,0).next







