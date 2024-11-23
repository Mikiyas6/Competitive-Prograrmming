# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy

        def fun(current,ptr1,ptr2,carry):
            
            if not ptr1 and not ptr2:
                if carry>0:
                    node = ListNode(carry)
                    current.next = node
                return current
            if not ptr1:
                total = ptr2.val + carry
                node = ListNode(total%10)
                carry = total//10
                current.next = fun(node,None,ptr2.next,carry)
                return current
            if not ptr2:
                total = ptr1.val + carry
                node = ListNode(total%10)
                carry = total//10
                current.next = fun(node,ptr1.next,None,carry)
                return current
            total = ptr1.val + ptr2.val + carry
            node = ListNode(total%10)
            carry = total//10
            current.next = fun(node,ptr1.next,ptr2.next,carry)
            return current
        
        return fun(current,l1,l2,0).next