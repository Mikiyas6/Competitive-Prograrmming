# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        unsorted_part = head.next
        head.next = None
        sorted_part = head

        def fun(sorted_part, unsorted_part):
            if not unsorted_part:
                return sorted_part

            unsorted_second_part = unsorted_part.next
            unsorted_part.next = None
            second_node = unsorted_part

            if second_node.val < sorted_part.val:
                second_node.next = sorted_part
                sorted_part = second_node
            else:
                current = sorted_part
                while current.next:
                    if second_node.val <= current.next.val:
                        broken_part = current.next
                        current.next = second_node
                        second_node.next = broken_part
                        break
                    current = current.next
                
                else:
                    current.next = second_node

            return fun(sorted_part, unsorted_second_part)

        return fun(sorted_part, unsorted_part)
