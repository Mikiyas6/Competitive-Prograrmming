# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
#         if not head or not head.next:
#             return head

#         def fun(left, right, head):
#             if not head.next:
#                 if head.val < x:
#                     left.next = ListNode(head.val)
#                 else:
#                     right.next = ListNode(head.val)
#                 return left.next, right.next

#             Node = ListNode(head.val)
#             if head.val < x:
#                 left.next = Node
#                 return fun(left.next, right, head.next)
#             else:
#                 right.next = Node
#                 return fun(left, right.next, head.next)

#         dummy_left = ListNode(-1)
#         dummy_right = ListNode(-1)
        
#         left, right = fun(dummy_left,dummy_right, head)

#         current = dummy_left
#         while current.next:
#             current = current.next
#         current.next = dummy_right.next

#         return dummy_left.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        def fun(current, head,side):
            if not head.next:
                if (head.val < x and side == "less") or( head.val >= x and side == "greater"):
                    Node = ListNode(head.val)
                    current.next = Node
                return current

            if (head.val < x and side == "less") or( head.val >= x and side == "greater"):
                Node = ListNode(head.val)
                current.next =  fun(Node, head.next, side)
                return current
            
            else:

                return fun(current,head.next,side)

        less = fun(ListNode(-1),head,"less") 
        greater = fun(ListNode(-1),head,"greater")

        if not less.next:

            return greater.next
        current = less.next
        while current.next:
            current = current.next
        current.next = greater.next

        return less.next