# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = list1
        prev_a = dummy

        for _ in range(a):
            prev_a = prev_a.next

        cur_b = prev_a
        for _ in range(b - a + 2):
            cur_b = cur_b.next

        last_list2 = list2
        while last_list2.next:
            last_list2 = last_list2.next

        prev_a.next = list2
        last_list2.next = cur_b

        return dummy.next
