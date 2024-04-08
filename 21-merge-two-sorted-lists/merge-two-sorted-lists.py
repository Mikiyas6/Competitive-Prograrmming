# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1) # A chekal pointer who is going to point at that node forever
        current = dummy # A pointer that points to the end of the node

        # dummy
        #  ↓
        #  O → O → O
        #          ↑
        #          current

        def fun(current,list1,list2):

            if not list1:

                current.next = list2

                return current

            if not list2:

                current.next = list1

                return current
            
            if list1.val <= list2.val:

                current.next = list1
                list1 = list1.next
            
            else:

                current.next = list2
                list2 = list2.next

            current.next = fun(current.next,list1,list2)

            return current
    
        return fun(current,list1,list2).next



        