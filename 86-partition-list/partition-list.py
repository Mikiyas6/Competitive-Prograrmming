# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next:

            return head

        def fun(left, right, head, x):
            if not head:
                return left.next, right.next

            if head.val < x:
                left.next = ListNode(head.val)
                return fun(left.next, right, head.next, x)
            else:
                right.next = ListNode(head.val)
                return fun(left, right.next, head.next, x)

        dummy_left = ListNode(-1)
        dummy_right = ListNode(-1)
        left, right = fun(dummy_left, dummy_right, head, x)

        current = dummy_left
        while current.next:
            current = current.next
        current.next = dummy_right.next

        return dummy_left.next




        
    # def get_middle(list2):

        #     if not list2 or not list2.next:

        #         return list2

        #     slow = list2
        #     fast = list2.next

        #     while fast and fast.next:

        #         slow = slow.next
        #         fast = fast.next.next

        #     return slow
        
        # def sort(list2):

        #     if not list2 or not list2.next:

        #         return list2
            
        #     middle = get_middle(list2)
        #     right_half = middle.next
        #     middle.next = None
        #     left_half = list2

        #     left = sort(left_half)
        #     right = sort(right_half)

        #     merged = merge(left,right)

        #     return merged

        # def merge(list1,list2):
            
        #     dummy = ListNode(-1)
        #     current = dummy

        #     def fun(current,list1,list2): 

        #         if not list1:

        #             current.next = list2
                
        #             return current
                
        #         if not list2:

        #             current.next = list1

        #             return current
                
        #         if list1.val <= list2.val:

        #             value = list1.val
        #             list1 = list1.next
                
        #         else:

        #             value = list2.val
        #             list2 = list2.next
                
        #         Node = ListNode(value)

        #         current.next = fun(Node,list1,list2)

        #         return current
            
        #     return fun(current,list1,list2).next
        
        # current = head

        # while current.val != x:

        #     current = current.next

        # list2 = current.next
        # list2 = sort(list2)
        # current.next = None
        # list1 = head

        # return merge(list1,list2)