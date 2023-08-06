# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 and list2:
            value = list2.val
            list2 = list2.next
            return ListNode(value,self.mergeTwoLists(list1,list2))
        elif list1 and not list2:
            value = list1.val
            list1 = list1.next
            return ListNode(value,self.mergeTwoLists(list1,list2))
        else:
            if list1.val <= list2.val:
                value = list1.val
                list1 = list1.next
                return ListNode(value,self.mergeTwoLists(list1,list2))
            else:
                value = list2.val
                list2 = list2.next
                return ListNode(value,self.mergeTwoLists(list1,list2))



