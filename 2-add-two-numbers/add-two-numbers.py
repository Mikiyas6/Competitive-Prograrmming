# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy
        def fun(current,node1,node2,carry):

            if not node1 and not node2:
                if carry > 0:
                    current.next = ListNode(carry)
                return current
            if not node2 and node1:
                value1 = node1.val
                value2 = 0
            elif not node1 and node2:
                value1 = 0
                value2 = node2.val
            else:
                value1 = node1.val
                value2 = node2.val
            total = value1 + value2 + carry
            newNode = ListNode(total%10)
            carry = total // 10
            if node1:
                next1 = node1.next
            else:
                next1 = None
            if node2:
                next2 = node2.next
            else:
                next2 = None
            current.next = fun(newNode,next1,next2,carry)
            return current
        
        return fun(current,l1,l2,0).next