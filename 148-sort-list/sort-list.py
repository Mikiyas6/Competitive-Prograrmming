# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:

            return head
        
        def get_middle(head):

            if not head or not head.next:

                return head
            
            slow = head
            fast = head.next

            while fast and fast.next:

                slow = slow.next
                fast = fast.next.next
            
            return slow

        def merge(list1,list2):

            dummy = ListNode(-1)
            current = dummy

            def fun(current,list1,list2):

                if not list1:

                    current.next = list2

                    return current
                
                if not list2:

                    current.next = list1

                    return current
                
                if list1.val <= list2.val:

                    value = list1.val
                    list1 = list1.next
                
                else:

                    value = list2.val
                    list2 = list2.next
                
                Node = ListNode(value)

                current.next = fun(Node,list1,list2)

                return current
            
            return fun(current,list1,list2).next

        def final(head):

            if not head.next:

                return head
            
            middle = get_middle(head)

            right_part = middle.next
            middle.next = None
            left_part = head

            left_part = final(left_part)
            right_part = final(right_part)

            merged = merge(left_part,right_part)

            return merged
        
        return final(head)