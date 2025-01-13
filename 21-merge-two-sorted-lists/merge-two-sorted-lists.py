# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        def merge(list1,list2):
            dummy = ListNode(-1)
            current = dummy
            node1 = list1
            node2 = list2
            def merger(current,list1,list2):
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
                node = ListNode(value)
                current.next = merger(node,list1,list2)
                return current
            return merger(current,node1,node2).next
        return merge(list1,list2)