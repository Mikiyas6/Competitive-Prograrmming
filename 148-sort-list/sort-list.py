# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def fun(head):

            if not head or not head.next:

                return head
            
            left,right = get_middle(head) 
            left = fun(left)
            right = fun(right)

            return merge(left, right)
        
        def get_middle(head):

            if not head or not head.next:
                return head

            # Use fast-slow pointers to find the middle of the linked list
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # Split the linked list into two halves
            second_half = slow.next
            slow.next = None

            return head, second_half

        def merge(left,right):

            dummy = ListNode(-1)
            current = dummy

            def function(current,left,right):

                if not left:

                    current.next = right

                    return current
                
                if not right:

                    current.next = left

                    return current
                
                if left.val <= right.val:

                    value = left.val
                    left = left.next
                
                else:

                    value = right.val
                    right = right.next
                
                Node = ListNode(value)
                
                current.next = function(Node,left,right)

                return current
            
            return function(current,left,right).next
        
        return fun(head)